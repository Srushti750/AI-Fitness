from fastapi import APIRouter
from app.database.connection import client

dashboard_api = APIRouter()

@dashboard_api.get("/dashboard")
def dashboard():
    return {
        "message" : "dashboard API"
    }

from fastapi import APIRouter

@dashboard_api.get("/db-status")
def database_status():
    try:
        client.admin.command("ping")
        return {
            "database": "connected"
        }
    except Exception as e:
        return {
            "database": "disconnected",
            "error": str(e)
        }