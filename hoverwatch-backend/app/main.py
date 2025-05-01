from fastapi import FastAPI
from app.routes.logs import router as log_router
from app.routes.screenshots import router as screenshot_router

app = FastAPI(title="Hoverwatch Backend")

app.include_router(log_router, prefix="/api")
app.include_router(screenshot_router, prefix="/api")
