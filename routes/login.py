from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class UserLoginModel(BaseModel):
    email: str
    password: str


@router.post("/login")
def login(user: UserLoginModel):
    return {"access_token": "0ru3ljljdlfjdl"}
