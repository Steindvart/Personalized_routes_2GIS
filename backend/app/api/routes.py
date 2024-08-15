from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from .mock import router as mock_router
from .users import router as users_router
from .guide import router as guide_router
from .. import schemas, models

from ..models import Preference as PreferenceModel
from ..schemas import GlobalPreference, CurrentPreferences, GlobalPreferenceSimple

from ..db import get_db

router = APIRouter()
router.include_router(mock_router, prefix="/mock", tags=["mock"])
router.include_router(users_router, prefix="/users", tags=["users"])
router.include_router(guide_router, prefix="/guide", tags=["guide"])


@router.post('/generate-journey')
def generate_routes(cur_preferences: CurrentPreferences):
  if not cur_preferences.activities:
    raise HTTPException(status_code=400, detail="Activities list cannot be empty")

  # Здесь должна быть логика генерации маршрута на основе предпочтений (постоянный из БД + текущих из запроса)
  # Для примера выходных данных: ручная подстановка - что примерно ожидается для активностей "поесть", "погулять", "шопинг"
  generated_route = [
    {"step": 1, "place": "Новосибирск, Кафе \"Подсолнух\", ​Площадь Карла Маркса, 10"},
    {"step": 2, "place": "Новосибирск, Сквер им. Сибиряков-Гвардейцев"},
    {"step": 3, "place": "Новосибирск, Сан Сити - многофункциональный центр, ​Площадь Карла Маркса, 7"},
  ]

  return {"status": "success", "data": generated_route, "echo": cur_preferences}


@router.post("/preferences/simple")
def update_global_preferences(preferences: schemas.GlobalPreferenceSimple, db: Session = Depends(get_db)):
  user_id = 1  # Заменить на current_id по токену

  # Удаляем старые предпочтения
  db.query(models.Preference).filter(models.Preference.user_id == user_id).delete()

  # Сохраняем новые предпочтения
  categories = ["food", "walk", "fun", "style"]
  for category_name in categories:
    category = db.query(models.Category).filter(models.Category.name == category_name).first()
    if category:
      for option in getattr(preferences, category_name):
        new_preference = models.Preference(
          user_id=user_id,
          category_id=category.id,
          options=option,
          rating=5.0
        )
        db.add(new_preference)
  db.commit()

  return {"status": "success", "preferences": preferences}

@router.get("/users/{id}/preferences", response_model=GlobalPreferenceSimple)
def get_global_preferences(id: int, db: Session = Depends(get_db)):
  # заменить на current_user
  preferences = db.query(models.Preference).filter(models.Preference.user_id == id).all()

  user_preferences = {
      "food": [],
      "walk": [],
      "fun": [],
      "style": []
  }

  for pref in preferences:
      category_name = db.query(models.Category).filter(models.Category.id == pref.category_id).first().name.lower()
      if category_name in user_preferences:
          user_preferences[category_name].append(pref.options)

  response = GlobalPreferenceSimple(
      food=user_preferences["food"],
      walk=user_preferences["walk"],
      fun=user_preferences["fun"],
      style=user_preferences["style"]
  )

  return response
