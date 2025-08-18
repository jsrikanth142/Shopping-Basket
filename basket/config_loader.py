import json
from decimal import Decimal
from pathlib import Path
from config.settings import CATALOGS_DIR, OFFERS_DIR, DEFAULT_BRANCH
import logging

logger = logging.getLogger("basket")

def safe_load_json(file_path: Path):
    try:
        with open(file_path, "r") as f:
            return json.load(f)
    except json.JSONDecodeError as e:
        logger.error("Invalid JSON", extra={"extra_data": {"file": str(file_path), "error": str(e)}})
        raise
    except FileNotFoundError:
        logger.error("Config file missing", extra={"extra_data": {"file": str(file_path)}})
        raise

def load_catalog(branch: str = DEFAULT_BRANCH) -> dict:
    file_path = CATALOGS_DIR / f"{branch}.json"
    if not file_path.exists():
        file_path = CATALOGS_DIR / f"{DEFAULT_BRANCH}.json"
    data = safe_load_json(file_path)
    return {k: Decimal(v["price"]) for k, v in data.items()}

def load_offers(branch: str = DEFAULT_BRANCH) -> list:
    file_path = OFFERS_DIR / f"{branch}.json"
    if not file_path.exists():
        file_path = OFFERS_DIR / f"{DEFAULT_BRANCH}.json"
    return safe_load_json(file_path)
