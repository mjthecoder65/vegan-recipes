from pydantic import BaseModel


class Recipe(BaseModel):
    title: str
    description: str
    steps: list[str]
    image: str
    cartegory: str


class Cartegory(BaseModel):
    title: str
