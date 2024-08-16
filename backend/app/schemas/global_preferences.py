from enum import Enum

from pydantic import BaseModel

class FoodPref(str, Enum):
  cafe = 'Кафе'
  restaurant = 'Рестораны'
  fastFood = 'Фаст-фуд'

class FoodStylePref(str, Enum):
  european = 'Европейская кухня'
  asian = 'Азиатская кухня'

class WalkPref(str, Enum):
  park = 'Парки'
  attraction = 'Достопримечательности'
  architecture = 'Архитектура'

class FunPref(str, Enum):
  anticafe = 'Антикафе'
  pub = 'Бар'
  karaoke = 'Караоке'
  european = 'Европейская кухня'
  games = 'Игры/Видеоигры'

class StylePref(str, Enum):
  noisy = 'Шумный'
  calm = 'Спокойный'
  party = 'Для компании'
  alone = 'Одному'


class GlobalPreferenceSimple(BaseModel):
  food: list[FoodPref]
  foodStyle: list[FoodStylePref]
  walk: list[WalkPref]
  fun: list[FunPref]
  style: list[StylePref]
