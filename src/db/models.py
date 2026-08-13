"""
src/db/models.py - the structured fleet-ops schema: chassis, technicians, maintenance
events, and campaigns. This is the "structured data" counterpart to data/documents/ - the
same real-world facts (chassis maintenance, in repair_bay_logs.csv) sometimes belong in a
proper relational DB instead of a document, because a question like "how many times has
the Scout Chassis needed thruster repairs" needs an exact COUNT, not an LLM eyeballing a handful
of retrieved chunks. See src/nl2sql/ for how natural language reaches these tables.
"""

from sqlalchemy import Column, Integer, String, Text, Numeric, Date, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class Chassis(Base):
    __tablename__ = "chassis"

    id = Column(Integer, primary_key=True)
    chassis_class = Column(String, unique=True, nullable=False)
    status = Column(String, nullable=False)  # combat_ready | needs_maintenance | in_storage | decommissioned
    energon_core_pct = Column(Numeric, nullable=False)
    last_diagnostic_date = Column(Date, nullable=False)

    maintenance_events = relationship("MaintenanceEvent", back_populates="chassis")
    campaigns = relationship("Campaign", back_populates="chassis")


class Technician(Base):
    __tablename__ = "technicians"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    specialty = Column(String, nullable=False)
    years_experience = Column(Integer, nullable=False)

    maintenance_events = relationship("MaintenanceEvent", back_populates="technician")


class MaintenanceEvent(Base):
    __tablename__ = "maintenance_events"

    id = Column(Integer, primary_key=True)
    chassis_id = Column(Integer, ForeignKey("chassis.id"), nullable=False)
    technician_id = Column(Integer, ForeignKey("technicians.id"), nullable=False)
    event_date = Column(Date, nullable=False)
    component = Column(String, nullable=False)
    issue = Column(Text, nullable=False)
    resolution = Column(Text, nullable=False)
    resolution_hours = Column(Numeric, nullable=False)
    cost_usd = Column(Numeric, nullable=False)

    chassis = relationship("Chassis", back_populates="maintenance_events")
    technician = relationship("Technician", back_populates="maintenance_events")


class Campaign(Base):
    __tablename__ = "campaigns"

    id = Column(Integer, primary_key=True)
    chassis_id = Column(Integer, ForeignKey("chassis.id"), nullable=False)
    campaign_date = Column(Date, nullable=False)
    location = Column(String, nullable=False)
    threat_level = Column(Integer, nullable=False)  # 1 (routine) - 5 (extinction-level)
    duration_min = Column(Integer, nullable=False)
    outcome = Column(String, nullable=False)  # success | partial | aborted

    chassis = relationship("Chassis", back_populates="campaigns")
