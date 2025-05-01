from fastapi import APIRouter
from app.models import LogEntry
from app.db import db

router = APIRouter()

@router.post("/logs")
async def receive_log(log: LogEntry):
    await db.logs.insert_one(log.dict())
    return {"status": "log saved"}
