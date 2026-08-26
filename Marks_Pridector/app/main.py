from fastapi import FastAPI
import uvicorn
from model import model

app = FastAPI()

@app.get("/")
def first_page():
    return {"messege" : "Hello world"}

@app.get("/model")
def model_status():
    
    