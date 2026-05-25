from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.db.database import get_db

from app.models.user import User

from app.schemas.user import UserCreate
from app.schemas.user import UserResponse

router = APIRouter()


@router.post("/users", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = User(
        email=user.email, full_name=user.full_name, hashed_password=user.password
    )

    db.add(db_user)

    db.commit()

    db.refresh(db_user)

    return db_user
