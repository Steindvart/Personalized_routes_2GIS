from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from .mock import router as mock_router
from .users import router as users_router
from .guide import router as guide_router

from ..models import Preference as PreferenceModel
from ..schemas import GlobalPreference, CurrentPreferences

from ..db import get_db

router = APIRouter()
router.include_router(mock_router, prefix="/mock", tags=["mock"])
router.include_router(users_router, prefix="/users", tags=["users"])
router.include_router(guide_router, prefix="/guide", tags=["guide"])


@router.post('/generate-journey')
def generate_routes(cur_preferences: CurrentPreferences):

  if not cur_preferences.activities:
    raise HTTPException(status_code=400, detail="Activities list cannot be empty")

  # Логика генерации маршрута на основе предпочтений
  # Это может быть обращение к базе данных, алгоритмы расчета маршрутов и т.д.
  # Для примера: ручная подстановка данных - что примерно ожидается для активностей "поесть", "погулять", "шопинг"
  generated_route = [
    {"step": 1, "place": "Новосибирск, Кафе \"Подсолнух\", ​Площадь Карла Маркса, 10"},
    {"step": 2, "place": "Новосибирск, Сквер им. Сибиряков-Гвардейцев"},
    {"step": 3, "place": "Новосибирск, Сан Сити - многофункциональный центр, ​Площадь Карла Маркса, 7"},
  ]

  return {"status": "success", "data": generated_route}


# Эндпоинты для работы с предпочтениями
@router.post("/preferences/", response_model=GlobalPreference)
def create_preference(user_id: int, category_id: int, rating: float, options: str, db: Session = Depends(get_db)):
  db_preference = PreferenceModel(user_id=user_id, category_id=category_id, rating=rating, options=options)
  db.add(db_preference)
  db.commit()
  db.refresh(db_preference)
  return db_preference
