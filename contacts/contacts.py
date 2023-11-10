from uuid import UUID

from fastapi import HTTPException, APIRouter

from users.models import UserCreate
from storage.fake_db import fake_db

contacts_router = APIRouter()


@contacts_router.get("/api/contacts")
def get_all_contacts():
    users = fake_db.get("users", {}).values()
    for user in users:
        print(user)
    return list(users)


@contacts_router.get("/api/contacts/{user_id}", response_model=UserCreate)
def get_contact(user_id: UUID):
    user = fake_db.get("users", {}).get(str(user_id))

    if user is None:
        raise HTTPException(status_code=404, detail="User not found.")
    return user
