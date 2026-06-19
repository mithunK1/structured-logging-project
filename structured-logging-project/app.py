import logging
import json
from datetime import datetime
from flask import Flask

app = Flask(__name__)

class JsonFormatter(logging.Formatter):
    def format(self, record):
        log_record = {
            "timestamp": datetime.utcnow().isoformat(),
            "service": "sample-backend",
            "level": record.levelname,
            "message": record.getMessage()
        }
        return json.dumps(log_record)

logger = logging.getLogger()
handler = logging.StreamHandler()
handler.setFormatter(JsonFormatter())
logger.addHandler(handler)
logger.setLevel(logging.INFO)

@app.route("/")
def home():
    logger.info("Home endpoint accessed")
    return {"HI": "SCSVMV DEEMED UNIVERSITY!"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=12345)
