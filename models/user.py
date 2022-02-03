from pydantic import BaseModel


class User(BaseModel):
    email: str
    phone: str
    password: str
    image: str
