from fastapi import APIRouter, Response, HTTPException
from fastapi.responses import JSONResponse, RedirectResponse, FileResponse
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel

router = APIRouter()


class UserLoginModel(BaseModel):
    email: str
    password: str


@router.post("/login")
def login(user: UserLoginModel, response: Response):
    print(user)
    print(response)
    # response.headers["X-Auth-Token"] = "token"
    headers = {"X-Auth-Token": "Token"}
    content = {"ok": True, "message": "Logged in"}
    return JSONResponse(content=content, status_code=400, headers=headers)


@router.get("/")
async def main():
    file_path = "michael.jpg"
    return FileResponse(file_path)


@router.get("/api/images/{id}", response_class=FileResponse)
async def stream_file(id: int, response: Response):
    response.set_cookie(key="email", value="test@example.com")  # Cookie
    file_path = "michael.jpg"
    return FileResponse(file_path)


# How to set cookies
@router.get("/api/cookie")
async def create_cookie():
    content = {"message": "Come to the dark side, we have cookies"}
    res = JSONResponse(content=content, status_code=200)
    res.set_cookie(key="email", value="foo@fastapi.com")
    res.set_cookie(key="username", value="mjthecoder")
    return res
