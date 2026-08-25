from fastapi import FastAPI
import uvicorn
app = FastAPI()

@app.get("/")
def first_page():
    return {"messege" : "Hello world"}