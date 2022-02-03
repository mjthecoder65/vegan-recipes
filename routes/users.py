from fastapi import APIRouter
from models.user import User

router = APIRouter()


@router.post("/api/users", tags=["Users"])
def create_user(user: User):
    # Return JSON webtoken
    return {}


@router.get("/me")
def get_user():
    return {}
