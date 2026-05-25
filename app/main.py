from fastapi import FastAPI

from app.db.database import Base
from app.db.database import engine


app = FastAPI()

Base.metadata.create_all(bind=engine)


@app.get("/")
def root():
    return {"message": "API is running"}
