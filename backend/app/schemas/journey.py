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

  def from_dict(src: dict, type: JourneyPlaceType):
    return JourneyPlace(
      type=type,
      name=src["name"],
      address=f'{src["address_name"]}, {src.get("address_comment", "")}',
      desc=f'',
      rating=src["reviews"]["rating"],
      point=(src["point"]["lat"], src["point"]["lon"])
    )


class Journey(BaseModel):
  places: list[JourneyPlace]
