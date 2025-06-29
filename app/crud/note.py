from app.db import db 
from app.models.note import NoteCreate, NoteUpdate
from bson import ObjectId

notes_collection = db["notes"]
# note create
async def create_note(note: NoteCreate):
    note_data = note.model_dump()
    note_data["user_id"] = ObjectId(note_data["user_id"])
    await notes_collection.insert_one(note_data)
    return True

# get note
async def get_note(note_id: str):
    return await notes_collection.find_one({"_id": ObjectId(note_id)}) 

# get notes 
async def get_notes():
    return await notes_collection.find().to_list() 

# update note
async def update_note(note_id: str, note: NoteUpdate):
    result = await notes_collection.update_one(
        {"_id": ObjectId(note_id)},
        {"$set": {**note.model_dump(exclude_unset=True)}}
    )  
    return result.modified_count > 0 

# deltet note
async def delete_note(note_id: str):
    result = await notes_collection.delete_one({"_id": ObjectId(note_id)}) 

    return result.deleted_count > 0 