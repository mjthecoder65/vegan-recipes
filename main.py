import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def vegan_home():
    return {"message": "A healthy inside starts from inside"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=3000, reload=True)
