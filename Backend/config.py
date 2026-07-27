# NOTE: not part of the original Copilot output — minimal config stub added
# so app.py has settings to grow into. Values are read from environment
# variables; nothing sensitive is hardcoded here.

import os


class Settings:
    APP_NAME = "Hybrid Photo-to-MLS Narrative Engine"
    AZURE_STORAGE_CONNECTION_STRING = os.getenv("AZURE_STORAGE_CONNECTION_STRING", "")
    AZURE_STORAGE_CONTAINER = os.getenv("AZURE_STORAGE_CONTAINER", "listing-photos")
    NWMLS_COMPLIANCE_MODE = os.getenv("NWMLS_COMPLIANCE_MODE", "strict")


settings = Settings()
