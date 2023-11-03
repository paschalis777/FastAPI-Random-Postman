from fastapi import FastAPI
import random


app = FastAPI()

@app.get("/")
async def root():
    return {"message": "hello world"}

@app.get("/random/{limit}")
async def get_random (limit: int):
    rn: int =random.randint(0, limit)
    return {"number " : rn ,"limit:" : limit}



# uvicorn main:app --reload