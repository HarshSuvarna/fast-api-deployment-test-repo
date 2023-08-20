from fastapi import FastAPI
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

@app.get('/')
def index():
    return {"message": f"Hellos TEST HARSH", "secrets":os.getenv('SECRET')}



