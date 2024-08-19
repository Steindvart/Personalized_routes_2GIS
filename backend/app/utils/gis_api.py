import requests
from typing import Optional
from enum import Enum

import logging as log

from ..config import T_GIS_API_KEY

CATALOG_API_URL: str = 'https://catalog.api.2gis.com'
PLACES_API_ENDPOINT: str = '/3.0/items'
GEOCODE_API_ENDPOINT: str = '/3.0/items/geocode'

ROUTING_API_URL: str = 'http://routing.api.2gis.com'
DISTANCE_API_ENDPOINT: str = '/get_dist_matrix'

class PlaceType(Enum):
  ORG = 'branch'
  ATTRACTION = 'attraction'
  BUILDING = 'building'

  def __str__(self):
    return self.value


class GisPoint():
  def __init__(self, lon: float, lat: float) -> None:
    self.lon: float = lon
    self.lat: float = lat


# TODO - type for fields param


class GisApi:
  # ----- Common ------
  def __init__(self, api_key: str) -> None:
    self.api_key = api_key


  def _make_request(self, url: str, params: dict | None = None, body: dict | None = None, method: str = "GET") -> dict:
    """Внутренний метод для выполнения HTTP-запросов к API."""
    log.debug(url)

    params = params or {}
    params['key'] = self.api_key

    if method == "POST":
      response = requests.post(url, params=params, json=body)
    elif method == "PUT":
      response = requests.put(url, params=params, json=body)
    elif method == "DELETE":
      response = requests.delete(url, params=params, json=body)
    else:
      response = requests.get(url, params=params)

    response.raise_for_status()
    return response.json()

  def _make_catalog_request(self, endpoint: str, params: dict) -> dict:
    url = f"{CATALOG_API_URL}{endpoint}"
    return self._make_request(url, params)

  def _make_routing_request(self, endpoint: str, body: dict) -> dict:
    url = f"{ROUTING_API_URL}{endpoint}"
    return self._make_request(url, {}, body, 'POST')

  def _get_catalog_all_items(self, endpoint: str, params: dict) -> Optional[list]:
    """Получить элементы со всех страниц пагинации данных."""
    items = []
    total_items = 0
    page = 1

    while True:
      params['page'] = page
      data = self._make_catalog_request(endpoint, params)

      result: dict = data.get('result', {})
      current_items: list = result.get('items', [])
      total_items: int = result.get('total', 0)

      items.extend(current_items)

      if len(items) >= total_items:
        break

      page += 1

    return items

  def _get_additional_fields(self) -> list:
    return [
      'items.point', 'items.full_address_name', 'items.reviews', 'items.rubrics'
    ]

  def _get_all_fields(self) -> list:
    return [
      'items.point', 'items.full_address_name', 'items.reviews', 'items.rubrics',
      'items.context'
    ]

  def _get_geoplace_additional_fields(self) -> list:
    return [
      'items.point', 'items.address', 'items.description'
    ]

  def get_place(self, place_id: int, additional_info: bool = False) -> Optional[dict]:
    endpoint = f'{PLACES_API_ENDPOINT}/byid'

    params = {
      'id': place_id,
    }

    if additional_info:
      params['fields'] = ','.join(self._get_additional_fields_list())

    items = self._get_catalog_all_items(endpoint, params)
    if not items:
      return None

    return items[0]

  def format_place_response(self, place: dict) -> dict:
    """Отформатировать ответ, исключая ненужные поля."""
    formatted_place = {
        'id': place.get('id'),
        'name': place.get('name'),
        'address': place.get('full_address_name'),
        'rating': place.get('reviews', {}).get('rating'),
        'point': place.get('point')
    }
    return formatted_place

  def get_place_info(self, place_id: int) -> Optional[dict]:
    """Получить отформатированную информацию о месте/заведении по его ID."""
    place = self.get_place(place_id, True)
    if not place:
        return None

    return self.format_place_response(place)

  # ----- Getting city ------
  def get_city_id(self, city: str) -> Optional[int]:
    """Получить ID города по его названию."""
    endpoint = "/2.0/region/search"
    params = {"q": city}

    data = self._make_catalog_request(endpoint, params)

    regions = data.get('result', {}).get('items', [])
    if regions:
      return regions[0].get('id')
    return None


  # ----- Rubrics of city/region ------
  def list_city_general_rubrics(self, city_id: int, sub_rubrics: bool = False) -> Optional[list]:
    """Получить список общих рубрик города."""
    endpoint = "/2.0/catalog/rubric/list"

    params = {"region_id": city_id}
    if (sub_rubrics): params['fields'] = 'items.rubrics'

    return self._get_catalog_all_items(endpoint, params)


  def list_city_rubrics_by_parent(self, city_id: int, parent_id: int, sub_rubrics: bool = False) -> Optional[list]:
    """Получить список рубрик города по id родительской рубрики."""
    endpoint = "/2.0/catalog/rubric/list"

    params = {
      "region_id": city_id,
      "parent_id": parent_id
    }
    if (sub_rubrics): params['fields'] = 'items.rubrics'

    return self._get_catalog_all_items(endpoint, params)


  def search_city_rubrics(self, city_id: int, search: str, sub_rubrics: bool = False) -> Optional[list]:
    """Получить список рубрик города по поисковому запросу."""
    endpoint = "/2.0/catalog/rubric/search"

    params = {
      "region_id": city_id,
      "q": search
    }
    if (sub_rubrics): params['fields'] = 'items.rubrics'

    return self._get_catalog_all_items(endpoint, params)


  def get_city_rubric_info(self, city_id: int, rubric_id: int, sub_rubrics: bool = False) -> Optional[dict]:
    """Получить информацию о рубрике города по id рубрики."""
    endpoint = "/2.0/catalog/rubric/get"

    params = {
      "region_id": city_id,
      "id": rubric_id
    }
    if (sub_rubrics): params['fields'] = 'items.rubrics'

    items = self._get_catalog_all_items(endpoint, params)
    if (not items): return None

    return items[0]


  # ----- Places/Items ------
  def search_places(self, city: str, search: str, type: PlaceType = PlaceType.ORG) -> Optional[list]:
    """Получить список мест/заведений указанного города по поисковому запросу."""
    endpoint = PLACES_API_ENDPOINT

    params = {
      'q': f'{city} {search}',
      'type': str(type)
    }

    return self._get_catalog_all_items(endpoint, params)


  def search_places_by_point(self, search: str, point: GisPoint, radius: int = 500, type: PlaceType = PlaceType.ORG) -> Optional[list]:
    """Получить список мест/заведений в указанной локации по поисковому запросу."""
    endpoint = PLACES_API_ENDPOINT

    params = {
      'q': f'{search}',
      'type': str(type),
      'lon': point.lon,
      'lat': point.lat,
      'radius': radius
    }

    return self._get_catalog_all_items(endpoint, params)


  def get_place(self, place_id: int, additional_info: bool = False) -> dict | None:
    """Получить информацию о месте/заведении по его ID."""
    endpoint = f'{PLACES_API_ENDPOINT}/byid'

    params = {
      'id': place_id,
    }

    if (additional_info):
      params['fields'] = ','.join(self._get_additional_fields())

    items = self._get_catalog_all_items(endpoint, params)
    if (not items): return None

    return items[0]

  def get_place_all_info(self, place_id: int, additional_info: bool = False) -> dict | None:
    """Получить информацию о месте/заведении по его ID."""
    endpoint = f'{PLACES_API_ENDPOINT}/byid'

    params = {
      'id': place_id,
    }

    if (additional_info):
      params['fields'] = ','.join(self._get_all_fields())

    items = self._get_catalog_all_items(endpoint, params)
    if (not items): return None

    return items[0]

  def get_place_reviews(self, place_id: int) -> Optional[dict]:
    """Получить рейтинг места/заведения по его ID."""

    place = self.get_place(place_id, True)
    if (not place): return None

    return place.get('reviews', {})


  def get_place_attribute_groups(self, place_id: int) -> Optional[list]:
    """Получить группы дополнительных атрибутов места/заведения по его ID."""

    place = self.get_place(place_id, True)
    if (not place): return None

    return place.get('attribute_groups', {})


  # ----- Geocode ------
  def search_geoplaces_by_point(self, search: str, point: GisPoint, radius: int = 500, type: PlaceType = PlaceType.ATTRACTION) -> Optional[list]:
    """Получить список гео-мест в указанной локации по поисковому запросу."""
    endpoint = GEOCODE_API_ENDPOINT

    params = {
      'q': f'{search}',
      'type': str(type),
      'lon': point.lon,
      'lat': point.lat,
      'radius': radius,
      'fields': self._get_geoplace_additional_fields()
    }

    return self._get_catalog_all_items(endpoint, params)

  # ----- Distance ------
  def get_distance(self, point1: GisPoint, point2: GisPoint) -> Optional[int]:
    """Получить расстояние между двумя точками в метрах."""
    endpoint = DISTANCE_API_ENDPOINT

    body: dict = {
      "points": [
        {"lat": point1.lat, "lon": point1.lon},
        {"lat": point2.lat, "lon": point2.lon}
      ],
      "sources": [0],
      "targets": [1]
    }

    data = self._make_routing_request(endpoint, body)
    routes = data.get('routes', {})
    distance = routes[0].get('distance', 0)

    return distance


main_gis_api: GisApi = GisApi(T_GIS_API_KEY)