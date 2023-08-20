from fastapi import FastAPI
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

@app.get('/')
def index():
    return {"message": f"If secret somesr", "secrets":os.getenv('SECRET')}



