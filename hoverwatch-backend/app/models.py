from pydantic import BaseModel
from datetime import datetime

class LogEntry(BaseModel):
    device_id: str
    log: str
    timestamp: datetime
