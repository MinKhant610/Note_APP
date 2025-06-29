from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class UserRegister(BaseModel):
    id: Optional[str] = None
    name: str
    email: str 
    password: str  
    created_at: Optional[datetime] = datetime.now()
    updated_at: Optional[datetime] = datetime.now()

class UserLogin(BaseModel):
    email: str 
    password: str  
