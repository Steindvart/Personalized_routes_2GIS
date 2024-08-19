from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from .mock import router as mock_router
from .users import router as users_router
from .guide import router as guide_router

from ..models import Preference as PreferenceModel
from ..models.recomendations import RecommendationsEngine
from ..schemas import GlobalPreference, CurrentPreferences
from ..schemas.global_preferences import GlobalPreferenceSimple, single_preferences_obj

from ..db import get_db

user_selected_places = {
    "food": "70000001017381379",
    "fun": "70000001081855851",
    "walk": "70000001027445760"
}

router = APIRouter()
router.include_router(mock_router, prefix="/mock", tags=["mock"])
router.include_router(users_router, prefix="/users", tags=["users"])
router.include_router(guide_router, prefix="/guide", tags=["guide"])


@router.post('/generate-journey')
def generate_routes(cur_preferences: CurrentPreferences):

  if not cur_preferences.activities:
    raise HTTPException(status_code=400, detail="Activities list cannot be empty")

  engine: RecommendationsEngine = RecommendationsEngine(single_preferences_obj, cur_preferences)
  journey = engine.generateJourney()

  return {"status": "success", "data": journey, "echo": cur_preferences}


# Эндпоинты для работы с предпочтениями
@router.post("/preferences", response_model=GlobalPreference)
def create_preference(user_id: int, category_id: int, rating: float, options: str, db: Session = Depends(get_db)):
  db_preference = PreferenceModel(user_id=user_id, category_id=category_id, rating=rating, options=options)
  db.add(db_preference)
  db.commit()
  db.refresh(db_preference)
  return db_preference


@router.get("/preferences/simple")
def get_simple_preferences():
  global single_preferences_obj

  return {"status": "success", "preferences": single_preferences_obj}


@router.post("/preferences/simple")
def update_simple_preferences(preferences: GlobalPreferenceSimple):
  global single_preferences_obj
  single_preferences_obj = preferences

  return {"status": "success", "preferences": single_preferences_obj}
