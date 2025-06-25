from fastapi import APIRouter, HTTPException, status
from app.models.user import UserLogin, UserRegister
from app.crud.user import register_user, get_user_by_email 

router = APIRouter(prefix="")

@router.post("/register")
async def register(user: UserRegister):
    existing_user = await get_user_by_email(user.email)
    if existing_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User email already exists")
    await register_user(user)
    return {"message": "User Registered!"}

@router.post('/login')
async def login(user: UserLogin):
    db_user = await get_user_by_email(user.email)
    if not db_user or (user.password != db_user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invaild credentials")
    return {"message": "Login Success!"}