import uvicorn
from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import models
from database import engine, SessionLocal
from routers import depts, emps




app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

models.Base.metadata.create_all(bind=engine)
app.include_router(depts.router)
app.include_router(emps.router)

if __name__ == "__main__":
    uvicorn.run("profile-app-backend-api.main:app",
                port=8000, host='127.0.0.1', reload=True)