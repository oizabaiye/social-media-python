from fastapi import FastAPI

# create an instance of fast api
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello world"}