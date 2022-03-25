# https://qiita.com/satto_sann/items/4fbc1a4e2b33fa2237d2
from fastapi import FastAPI
from typing import List  # Required to define a nested Body.
from starlette.middleware.cors import CORSMiddleware
from db import session  # Session to connect with DB
from model import UserTable, User

app = FastAPI()

# Settings to avoid CORS.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -----API-----

@app.get("/")
def read_root():
    return {"Hello": "World"}

# Get all users.[GET]
@app.get("/users")
def read_users():
    users = session.query(UserTable).all()
    return users

# Get user matching id.[GET]
@app.get("/users/{user_id}")
def read_user(user_id: int):
    user = session.query(UserTable).\
        filter(UserTable.id == user_id).first()
    return user

# Register user.[POST]
@app.post("/user")
# /user?name="Emma"&age=5
async def create_user(name: str, age: int):
    user = UserTable()
    user.name = name
    user.age = age
    session.add(user)
    session.commit()

# Update usres information.[PUT]
@app.put("/user")
# {"id": 1, "name": "Emma", "age": 5}
async def update_user(new_user : User):
    user = session.query(UserTable).filter(UserTable.id == new_user .id).first()
    user.name = new_user .name
    user.age = new_user .age
    session.commit()