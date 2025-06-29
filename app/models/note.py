from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class NoteCreate(BaseModel):
    user_id: Optional[str] = None  
    title: str 
    description: str 
    created_at: Optional[datetime] = datetime.now()
    updated_at: Optional[datetime] = datetime.now()

class NoteUpdate(BaseModel):
    user_id: Optional[str] = None 
    title: Optional[str] = None 
    description: Optional[str] = None 
    updated_at: Optional[datetime] = datetime.now() 

class NoteResponse(BaseModel):
    id: str 
    user_id: str 
    title: str 
    description: str 
    created_at: datetime
    updated_at: datetime

    @classmethod
    def from_mongo(cls, note):
        return cls(
            id=str(note["_id"]),
            user_id=str(note["user_id"]),
            title=note["title"],
            description=note["description"],
            created_at=note["created_at"],
            updated_at=note["updated_at"]
        )