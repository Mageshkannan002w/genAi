"""
scripts/seed_db.py - populates the fleet-ops tables from the hand-authored, deterministic
rows in src/db/seed_data.py. Safe to re-run: clears the 4 tables (children before parents,
respecting foreign keys) and reinserts from scratch every time, so the DB always matches
whatever's currently in seed_data.py.

Run from the project root (after `python -m scripts.setup_db`):
    python -m scripts.seed_db
"""

from src.db.database import SessionLocal
from src.db.models import MaintenanceEvent, Campaign, Chassis, Technician
from src.db.seed_data import MAINTENANCE_EVENTS, CAMPAIGNS, CHASSIS_DATA, TECHNICIANS


def main():
    session = SessionLocal()
    try:
        # Children first - both have FKs into chassis/technicians.
        session.query(MaintenanceEvent).delete()
        session.query(Campaign).delete()
        session.query(Chassis).delete()
        session.query(Technician).delete()
        session.flush()

        chassis_by_class = {}
        for row in CHASSIS_DATA:
            chassis = Chassis(**row)
            session.add(chassis)
            chassis_by_class[row["chassis_class"]] = chassis

        technicians_by_name = {}
        for row in TECHNICIANS:
            tech = Technician(**row)
            session.add(tech)
            technicians_by_name[row["name"]] = tech

        session.flush()  # assigns .id to every chassis/technician before we reference them

        for row in MAINTENANCE_EVENTS:
            session.add(MaintenanceEvent(
                chassis_id=chassis_by_class[row["chassis"]].id,
                technician_id=technicians_by_name[row["technician"]].id,
                event_date=row["event_date"],
                component=row["component"],
                issue=row["issue"],
                resolution=row["resolution"],
                resolution_hours=row["resolution_hours"],
                cost_usd=row["cost_usd"],
            ))

        for row in CAMPAIGNS:
            session.add(Campaign(
                chassis_id=chassis_by_class[row["chassis"]].id,
                campaign_date=row["campaign_date"],
                location=row["location"],
                threat_level=row["threat_level"],
                duration_min=row["duration_min"],
                outcome=row["outcome"],
            ))

        session.commit()
        print(f"Seeded {len(CHASSIS_DATA)} chassis, {len(TECHNICIANS)} technicians, "
              f"{len(MAINTENANCE_EVENTS)} maintenance events, {len(CAMPAIGNS)} campaigns.")
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()


if __name__ == "__main__":
    main()
