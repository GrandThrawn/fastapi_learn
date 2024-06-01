# main.py
from typing_extensions  import Annotated
from fastapi import FastAPI

from contextlib import asynccontextmanager
from schemas import STask, STaskAdd
from database import create_tables, delete_tables
from router import router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print('clean db')
    await create_tables()
    print("create db")
    yield
    print("lifespan end")

app = FastAPI(lifespan=lifespan)
app.include_router(router)



@app.get("/")
async def root():
    return {"message": "Hello World again"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)