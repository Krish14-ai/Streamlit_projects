from fastapi import FastAPI
import uvicorn
from model.predictor import train

app = FastAPI()

@app.get("/")
def first_page():
    return {"messege" : "Hello world"}

@app.get("/model")
def model_status():
    train
    
    