from fastapi import FastAPI

from app.db.database import Base
from app.db.database import engine
from app.routes.user import router as user_router


app = FastAPI()
app.include_router(user_router)

Base.metadata.create_all(bind=engine)


@app.get("/")
def root():
    return {"message": "API is running"}
