from time import time
from fastapi import APIRouter, Request
from starlette.requests import Request

router = APIRouter()

# Implementing middleware, but not for authentication dude.
@router.middleware("http")
async def authenticate(request: Request, call_next):
    start_time = time()
    response = await call_next(request)
    process_time = time() - start_time()
    response.headers["X-Auth-Token"] = "Token"
    response.headers["X-Process-Time"] = process_time
    return response


__all__ = ["router"]
