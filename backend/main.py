from fastapi import FastAPI
from app.api.dashboard import dashboard_api as dashboard_router
from app.api.dashboard import dashboard_api as db_status

app = FastAPI()

app.include_router(
    dashboard_router,
    prefix="/app/fitness"
)

app.include_router(
    db_status,
    prefix="/app/fitness"
)

@app.get("/")
def home():
    return {
        "message": "AI Fitness Application Running Successfully"
    }
