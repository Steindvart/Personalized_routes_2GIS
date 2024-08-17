import difflib
import random

from ..schemas import CurrentPreferences, Activities

from ..schemas.currect_preferences import CurrentPreferences, Activities
from ..schemas.global_preferences import GlobalPreferenceSimple
from ..schemas.journey import Journey, JourneyPlace, JourneyPlaceType

from ..utils.gis_api import GisPoint, PlaceType, main_gis_api


RADIUS_DEFAULT: int = 1000
RADIUS_LIMIT: int = 5000

from typing import List, Dict, Optional

class RecommendationsEngine:
  def __init__(self, global_pref: GlobalPreferenceSimple, curr_pref: CurrentPreferences):
    self.global_pref: GlobalPreferenceSimple = global_pref
    self.curr_pref: CurrentPreferences = curr_pref

  def generateJourney(self) -> Journey:
    journey: Journey = Journey(
      places=[
        JourneyPlace(
          type=JourneyPlaceType.start,
          name='Стартовая точка',
          address='',
          desc='',
          rating=0,
          point=(self.curr_pref.point['lon'], self.curr_pref.point['lat'])
        )
      ]
    )

    unique_place_ids = set()

    for activity in self.curr_pref.activities:
      last_place = journey.places[-1]
      location = GisPoint(last_place.point[0], last_place.point[1])

      if activity == Activities.food:
        category: str = random.choice(self.global_pref.food)
        if category == 'Кафе': category = 'Кофейня'
        style: str = random.choice(self.global_pref.foodStyle)
        journey_place_type: JourneyPlaceType = JourneyPlaceType.food
        search: str = f'{category} {style}'

      elif activity == Activities.fun:
        category: str = random.choice(self.global_pref.fun)
        journey_place_type: JourneyPlaceType = JourneyPlaceType.fun
        search: str = f'{category}'

      elif activity == Activities.walk:
        category: str = random.choice(self.global_pref.walk)
        if category == 'Архитектура': category = 'Интересное здание'
        journey_place_type: JourneyPlaceType = JourneyPlaceType.walk
        search: str = f'{category}'

      radius = RADIUS_DEFAULT
      places: list[dict] = []

      while radius <= RADIUS_LIMIT:
        if activity != Activities.walk:
          places = main_gis_api.search_places_by_point(search, location, radius)
        else:
          places = main_gis_api.search_places_by_point(search, location, radius)

        if places:
          places = [place for place in places if place['id'] not in unique_place_ids]
          if places:
            break

        radius += RADIUS_DEFAULT

      if places:
        user_selected_places = self.curr_pref.activities[activity.value]
        best_place = self.find_most_similar_place(user_selected_places, places)
        if best_place:
          place_id = best_place['id']
          if activity != Activities.walk:
            place = main_gis_api.get_place(place_id, True)
          else:
            place = best_place

          journey_place: JourneyPlace = JourneyPlace.from_dict(place, journey_place_type)
          journey.places.append(journey_place)

          unique_place_ids.add(best_place['id'])
        else:
          # Логирование или обработка случая, когда не найдено подходящее место
          print(f"No similar places found for activity {activity}")
      else:
        # Логирование или обработка случая, когда нет доступных мест
        print(f"No places found for activity {activity}")

    return journey