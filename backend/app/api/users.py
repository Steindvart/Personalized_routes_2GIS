from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from .. import schemas, models

from app import schemas, models

from ..db import get_db

from app.exceptions.handlers import BadRequestException, NotFoundException

router = APIRouter()


@router.get("/", response_model=List[schemas.User])
def list_user(db: Session = Depends(get_db)):
  db_users = db.query(models.User).all()
  return db_users


@router.post("/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
  db_user_exists = db.query(models.User).filter(models.User.email == user.email).first()
  if db_user_exists:
    raise BadRequestException("User with a specified email already exists. Use another email.")
    # raise HTTPException(status_code=400, detail="User with a specified email already exists. Use another email.")
  db_user = models.User(email=user.email, name=user.name, password=user.password)
  db.add(db_user)
  db.commit()
  db.refresh(db_user)
  return db_user


@router.get("/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
  db_user = db.query(models.User).filter(models.User.id == user_id).first()
  if db_user is None:
    raise NotFoundException(id=user_id, dict_name="users")
    # raise HTTPException(status_code=404, detail="User not found")
  return db_user


@router.get("/{user_id}/preferences", response_model=List[schemas.GlobalPreference])
def read_user_preferences(user_id: int, db: Session = Depends(get_db)):
  preferences = db.query(models.Preference).filter(models.Preference.user_id == user_id).all()
  if not preferences:
    raise HTTPException(status_code=404, detail=f"Preferences for user_id={user_id} not found")
    # raise HTTPException(status_code=404, detail="Preferences not found")
  return preferences
