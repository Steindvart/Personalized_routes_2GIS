import random

from ..schemas import CurrentPreferences, Activities

from ..schemas.currect_preferences import CurrentPreferences, Activities
from ..schemas.global_preferences import GlobalPreferenceSimple, FoodPref
from ..schemas.journey import Journey, JourneyPlace, JourneyPlaceType

from ..utils.gis_api import GisPoint, PlaceType, main_gis_api

class RecommendationsEngine:
  def __init__(self, global_pref: GlobalPreferenceSimple, curr_pref: CurrentPreferences):
    self.global_pref: GlobalPreferenceSimple = global_pref
    self.curr_pref: CurrentPreferences = curr_pref


  def generateJourney(self) -> Journey:
    journey: Journey = Journey(places=[])

    for activity in self.curr_pref.activities:
      location: GisPoint = GisPoint(self.curr_pref.point['lat'], self.curr_pref.point['lon'])
      if (activity == Activities.food):
        category: str = random.choice(self.global_pref.food)
        if (category == 'Кафе'): category = 'Кофейня'

        style: str = random.choice(self.global_pref.foodStyle)
        type: PlaceType = PlaceType.ORG

        search: str = f'{category} {style}'

        places: list | None = main_gis_api.search_places_by_point(search, location, 1000, type)
        if places:
          selected_place = random.choice(places[:100])
          place_id = selected_place['id']
          place = main_gis_api.get_place(place_id, True)
          journey_place: JourneyPlace = JourneyPlace.from_dict(place, JourneyPlaceType.food)
          journey.places.append(journey_place)

    return journey
