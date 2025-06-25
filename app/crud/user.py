from app.db import db 
from app.models.user import UserRegister

users_collection = db["users"]

# User Register 
async def register_user(user: UserRegister):
    user_data = user.model_dump()
    result = await users_collection.insert_one(user_data)
    return UserRegister(id=str(result.inserted_id), **user_data)

# get user by email 
async def get_user_by_email(email: str):
    user = await users_collection.find_one({"email": email})
    if user:
        return UserRegister(id=str(user["_id"]), **user)
    return None 