from typing import Union
from fastapi import FastAPI

from contacts.contacts import contacts_router
from discussions.discussions import discussions_router
from users.users import users_router
from messages.messages import message_router

app = FastAPI()
app.include_router(users_router)
app.include_router(contacts_router)
app.include_router(discussions_router)
app.include_router(message_router)

# manager = ConnectionManager()

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
