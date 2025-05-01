from fastapi import APIRouter, File, UploadFile, Form
from datetime import datetime
import os
from app.db import db

router = APIRouter()

SCREENSHOT_DIR = "storage/screenshots"
os.makedirs(SCREENSHOT_DIR, exist_ok=True)

@router.post("/screenshots")
async def upload_screenshot(device_id: str = Form(...), file: UploadFile = File(...)):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"{device_id}_{timestamp}.png"
    filepath = os.path.join(SCREENSHOT_DIR, filename)

    with open(filepath, "wb") as f:
        f.write(await file.read())

    await db.screenshots.insert_one({"device_id": device_id, "filename": filename, "timestamp": datetime.now()})
    return {"status": "screenshot saved"}
