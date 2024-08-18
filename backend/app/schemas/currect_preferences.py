from enum import Enum

from pydantic import BaseModel


class Activities(str, Enum):
  food = 'Поесть'
  walk = 'Погулять'
  fun = 'Развлечься'
  shoping = 'Шопинг'


class CurrentPreferences(BaseModel):
  activities: list[Activities]
  averageCheck: int
  totalTime: int
  wayType: str
  wantSomethingNew: bool
  point: dict
