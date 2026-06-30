# Includes business logic

# Authentication of user through registration and login

from app.repositories.user_repository import UserRepository
from app.core.security import hash_password, verify_password
from app.models.user_model import UserModel
from app.core.jwt_handler import create_access_token

class AuthService:
    def register_user(register_data):
        existing_user = UserRepository.get_user_by_email(register_data.email)

        if existing_user:
            return {
                "message" : "Email is already registered"
            }
        
        hashed_password = hash_password(register_data.password)

        user = UserModel(
            username = register_data.username,
            email = register_data.email,
            password = hashed_password
        )

        inserted_data = UserRepository.create_user(user.to_dict())

        return {
            "message" : "User registered successfully",
            "user_id" : str(inserted_data)
        }

    def login_user(login_data):
        user = UserRepository.get_user_by_email(login_data.email)

        if not user:
            return {
                "message" : "Invalid email or password"
            }
        
        if not verify_password(login_data.password, user["password"]):
            return{
                "message" : "Invalid email or password"
            }
        
        access_token = create_access_token(
            {
                "sub" : str(user["_id"]),
                "email" : user["email"]
            }
        )

        return {
            "success" : True,
            "access_token" : access_token,
            "token_type" : "bearer"
        }