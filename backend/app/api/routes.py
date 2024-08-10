from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from .mock import router as mock_router
from .users import router as users_router
from .guide import router as guide_router

from ..models import Preference as PreferenceModel
from ..schemas import Preference

from ..db import get_db

router = APIRouter()
router.include_router(mock_router, prefix="/mock", tags=["mock"])
router.include_router(users_router, prefix="/users", tags=["users"])
router.include_router(guide_router, prefix="/guide", tags=["guide"])

# Эндпоинты для работы с предпочтениями
@router.post("/preferences/", response_model=Preference)
def create_preference(user_id: int, category_id: int, rating: float, options: str, db: Session = Depends(get_db)):
  db_preference = PreferenceModel(user_id=user_id, category_id=category_id, rating=rating, options=options)
  db.add(db_preference)
  db.commit()
  db.refresh(db_preference)
  return db_preference
