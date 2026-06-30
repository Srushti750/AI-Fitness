# Includes API routes

from fastapi import APIRouter
from app.schemas.user_schema import RegisterUserSchema, LoginUserSchema
from app.services.auth_service import AuthService

auth_api = APIRouter()

@auth_api.post("/register")
def register_user(register_data: RegisterUserSchema):
    return AuthService.register_user(register_data)

@auth_api.post("/login")
def login_user(login_data : LoginUserSchema):
    return AuthService.login_user(login_data)