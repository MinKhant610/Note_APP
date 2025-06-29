from fastapi import APIRouter, HTTPException, status
from app.models.user import UserLogin, UserRegister
from app.crud.user import register_user, get_user_by_email 
from app.utils.password import verify
from app.utils.authentication import generate_jwt_token

router = APIRouter(prefix="", tags=["Authentication"])

@router.post("/register")
async def register(user: UserRegister):
    existing_user = await get_user_by_email(user.email)
    if existing_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User email already exists")
    await register_user(user)
    token = generate_jwt_token({
        "name": existing_user.name,
        "email": existing_user.email
    })
    return{
        "message": "User Registered!",
        "token": token
    }

@router.post('/login')
async def login(user: UserLogin):
    db_user = await get_user_by_email(user.email)
    if not db_user or not verify(user.password, db_user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invaild credentials")
    # print(db_user.model_dump())
    token = generate_jwt_token({
        "id": db_user.id,
        "name": db_user.name,
        "email": db_user.email
    })
    return{
        "message": "User Login Success!",
        "token": token
    }