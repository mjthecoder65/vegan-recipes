from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from models.user import User
from pydantic import BaseModel

router = APIRouter()


@router.post("/api/users", tags=["Users"], status_code=200)
def create_user(user: User):
    # Return JSON webtoken
    content = {"username": "Michael", "password": "Gambia10@@dlj"}

    return JSONResponse(
        content=content, status_code=status.HTTP_201_CREATED, headers={}
    )


class User(BaseModel):
    id: str
    email: str
    username: str


@router.get("/me", response_model=User)
def get_user():
    return {
        "email": "mj@gmail.com",
        "username": "mjthecoder",
        "id": 1,
        "password": "ljdlfkd",
        "address": "Seoul, South Korea, Korea University",
    }
