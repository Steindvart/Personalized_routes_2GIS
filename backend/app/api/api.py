from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from .mock import api_router as mock_router
from .. import schemas, models

from ..models import User as UserModel, Preference as PreferenceModel
from ..schemas import UserCreate, User, Preference

from ..db import get_db

router = APIRouter()
router.include_router(mock_router, prefix="/mock", tags=["mock"])


# Эндпоинты для работы с пользователями
@router.post("/users/", response_model=User)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = UserModel(email=user.email, name=user.name, password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


@router.get("/users/{user_id}", response_model=User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = db.query(UserModel).filter(UserModel.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


# Эндпоинты для работы с предпочтениями
@router.post("/preferences/", response_model=Preference)
def create_preference(user_id: int, category_id: int, rating: float, options: str, db: Session = Depends(get_db)):
    db_preference = PreferenceModel(user_id=user_id, category_id=category_id, rating=rating, options=options)
    db.add(db_preference)
    db.commit()
    db.refresh(db_preference)
    return db_preference


@router.get("/users/{user_id}/preferences", response_model=List[schemas.Preference])
def read_user_preferences(user_id: int, db: Session = Depends(get_db)):
    preferences = db.query(models.Preference).filter(models.Preference.user_id == user_id).all()
    if not preferences:
        raise HTTPException(status_code=404, detail="Preferences not found")
    return preferences


