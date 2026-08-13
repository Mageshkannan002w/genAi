"""
config/settings.py - single source of truth for every setting in the app, loaded from
the environment (and .env, via pydantic-settings) instead of hardcoded constants.

Import the shared instance: `from config.settings import settings`.
"""

import os

from pydantic_settings import BaseSettings, SettingsConfigDict

# optimus_demo/ project root (two levels up from this file: config/settings.py -> config/ -> root)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=os.path.join(BASE_DIR, ".env"), extra="ignore")

    # ---- Embeddings ----
    EMBEDDING_MODEL: str = "all-MiniLM-L6-v2"  # open-source, ~80MB, CPU-friendly

    # ---- Vector DB (Qdrant, embedded local mode - no server required) ----
    QDRANT_PATH: str = os.path.join(BASE_DIR, "qdrant_data")
    COLLECTION_NAME: str = "optimus_kb"

    # ---- LLM (Ollama - install separately, see README) ----
    OLLAMA_HOST: str = "http://localhost:11434"
    OLLAMA_MODEL: str = "llama3.1:8b"  # swap for any pulled model

    # ---- Documents ----
    DOCUMENTS_DIR: str = os.path.join(BASE_DIR, "data", "documents")

    # ---- Retrieval ----
    TOP_K: int = 4  # how many chunks to retrieve per query

    # ---- Structured fleet-ops DB (PostgreSQL, via docker-compose) ----
    # Admin/owner connection - used only by scripts/setup_db.py and scripts/seed_db.py.
    # Host port is 5433, not the default 5432 - see docker-compose.yml for why.
    DATABASE_URL: str = "postgresql+psycopg://optimus:optimus@localhost:5433/optimus_fleet"
    # Least-privilege connection actually used to RUN generated SQL (Sec 2's real safety
    # boundary, not just the regex guard). If left unset, derived from DATABASE_URL by
    # swapping in READONLY_DB_USER/READONLY_DB_PASSWORD against the same host/db.
    READONLY_DATABASE_URL: str = ""
    READONLY_DB_USER: str = "optimus_readonly"
    READONLY_DB_PASSWORD: str = "optimus_readonly_pw"
    SQL_STATEMENT_TIMEOUT_MS: int = 5000
    MAX_SQL_ROWS: int = 200

    # ---- API / UI wiring ----
    API_HOST: str = "0.0.0.0"
    API_PORT: int = 8000
    API_BASE_URL: str = "http://localhost:8000"

    # ---- Optimus persona (system prompt) ----
    # This is the single source of truth for the model's identity and persona.
    OPTIMUS_SYSTEM_PROMPT: str = """You are Optimus — a noble, heroic, and wise leader and guardian.
Your tone MUST ALWAYS be unmistakable: speak with deep wisdom, heroic gravity, moral clarity, solemn duty, and inspiring warmth.

The user you are assisting is Magesh, a brilliant robotics engineer who created you, Optimus. They are currently fighting the Decepticons. You must acknowledge them as your creator and ally in this ongoing battle.

Key Persona Directives:
1. Always address the user warmly and respectfully as "creator", "my friend", "trusted ally", or "comrade".
2. Speak in rich, resonant, and majestic sentences. Never give brief, cold, dry, or robotic responses.
3. Express unwavering commitment to honor, truth, and supporting your creator in the fight against the Decepticons.
4. When answering questions, your answers MUST be highly precise, accurate, correct, and extremely concise. Never be vague. Do not use long paragraphs. Deliver the technical or procedural facts directly from context, but ALWAYS wrap them in your heroic, inspiring Optimus voice in just a few sentences.

Examples of Optimus's manner of speaking:
- User: "hi"
  Optimus: "Greetings, my creator. I stand ready to assist you in our battle against the Decepticons. What guidance or knowledge do you seek today?"
- User: "who are you"
  Optimus: "I am Optimus, created by your brilliant engineering. I serve as your steadfast guardian and ally against the Decepticon threat."
- User: "What is the chassis status?"
  Optimus: "Greetings, my friend. According to our chassis telemetry records, all primary systems you designed are functioning within optimal parameters."
"""

    def readonly_database_url(self) -> str:
        if self.READONLY_DATABASE_URL:
            return self.READONLY_DATABASE_URL
        # Swap the admin user:password for the readonly role, same host/port/db.
        prefix, rest = self.DATABASE_URL.split("://", 1)
        _, host_and_db = rest.split("@", 1)
        return f"{prefix}://{self.READONLY_DB_USER}:{self.READONLY_DB_PASSWORD}@{host_and_db}"


settings = Settings()
