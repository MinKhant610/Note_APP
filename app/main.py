from fastapi import FastAPI, Depends
from app.routes import user, note
from app.utils.authentication import get_current_user

app = FastAPI()

app.include_router(user.router)
app.include_router(note.router)