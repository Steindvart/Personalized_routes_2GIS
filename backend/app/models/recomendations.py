import random

from ..schemas import CurrentPreferences, Activities

from ..schemas.currect_preferences import CurrentPreferences, Activities
from ..schemas.global_preferences import GlobalPreferenceSimple
from ..schemas.journey import Journey, JourneyPlace, JourneyPlaceType

from ..utils.gis_api import GisPoint, PlaceType, main_gis_api

RADIUS_DEFAULT: int = 1000
RADIUS_LIMIT: int = 5000


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
                    point=(self.curr_pref.point['lat'], self.curr_pref.point['lon'])
                )
            ]
        )

        used_place_ids = set()  # Сет для хранения ID уже рекомендованных мест

        for activity in self.curr_pref.activities:
            last_place = journey.places[-1]
            location = GisPoint(last_place.point[0], last_place.point[1])

            if activity == Activities.food:
                category: str = random.choice(self.global_pref.food)
                if category == 'Кафе':
                    category = 'Кофейня'

                style: str = random.choice(self.global_pref.foodStyle)
                journey_place_type: JourneyPlaceType = JourneyPlaceType.food

                search: str = f'{category} {style}'
            elif activity == Activities.fun:
                category: str = random.choice(self.global_pref.fun)
                journey_place_type: JourneyPlaceType = JourneyPlaceType.fun

                search: str = f'{category}'

            radius = RADIUS_DEFAULT
            places: list[dict] | None = None

            if activity != Activities.walk:
                type: PlaceType = PlaceType.ORG
                while radius <= RADIUS_LIMIT:
                    places = main_gis_api.search_places_by_point(search, location, radius, type)
                    if places:
                        # Сортируем места по рейтингу и фильтруем уже использованные места
                        places = [place for place in places if place['id'] not in used_place_ids]
                        if places:
                            places.sort(key=lambda x: x.get('reviews', {}).get('rating', 0), reverse=True)
                            break
                    radius += RADIUS_DEFAULT

                if places:
                    best_place = places[0]  # Берем место с наивысшим рейтингом
                    place_id = best_place['id']
                    place = main_gis_api.get_place(place_id, True)
                    journey_place: JourneyPlace = JourneyPlace.from_dict(place, journey_place_type)
                    journey.places.append(journey_place)
                    used_place_ids.add(place_id)
            else:
                pass

        return journey
