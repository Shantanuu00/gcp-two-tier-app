from fastapi import FastAPI
import psycopg2
import os

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello from GCP 2-Tier App 🚀"}

@app.get("/health")
def health():
    return {"status": "ok"}
