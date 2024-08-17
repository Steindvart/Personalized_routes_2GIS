from enum import Enum
from pydantic import BaseModel

class JourneyPlaceType(str, Enum):
  start = 'start'
  food = 'food'
  walk = 'walk'
  fun = 'fun'
  shoping = 'shoping'


class JourneyPlace(BaseModel):
  type: JourneyPlaceType
  name: str
  address: str
  desc: str
  rating: float
  point: tuple[float, float]

  @staticmethod
  def from_dict(src: dict, type: JourneyPlaceType):
    if (type == JourneyPlaceType.walk):
      return JourneyPlace(
        type=type,
        desc='',
        address='',
        rating=0.0,
        name= src["name"],
        point=(src["point"]["lon"], src["point"]["lat"])
      )
    else:
      return JourneyPlace(
        type=type,
        name=src["name"],
        address=f'{src.get("address_name", '')}, {src.get("address_comment", '')}',
        desc='',
        rating=src.get("reviews", {}).get("rating", 0.0),  # Используем get с значением по умолчанию 0.0
        point=(src["point"]["lon"], src["point"]["lat"])
      )


class Journey(BaseModel):
  places: list[JourneyPlace]
