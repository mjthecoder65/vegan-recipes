# Cross Origin Resource Sharing (CORS)

# Different Origins because they use different protocals or ports
# http://localhost
# https://localhos:
# http://localhost:3000

from fastapi import APIRouter
from fastapi.middleware.cors import CORSMiddleware

router = APIRouter()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]

router.add_middleware(
    CORSMiddleware,
    allowed_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
    max_age=600,
)
