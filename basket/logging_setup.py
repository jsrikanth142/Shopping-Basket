import logging
import sys
from datetime import datetime
from decimal import Decimal
from config.settings import LOG_LEVEL

class JsonFormatter(logging.Formatter):
    def format(self, record):
        log_record = {
            "timestamp": datetime.utcnow().isoformat(),
            "level": record.levelname,
            "logger": record.name,
            "message": record.getMessage()
        }
        if hasattr(record, "extra_data"):
            log_record.update(record.extra_data)
        import json
        return json.dumps(log_record, default=lambda o: str(o))

def setup_logging():
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(JsonFormatter())
    logger = logging.getLogger("basket")
    logger.setLevel(LOG_LEVEL.upper())
    logger.handlers.clear()
    logger.addHandler(handler)
    return logger
