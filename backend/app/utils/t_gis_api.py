import requests
from typing import Optional
from enum import Enum

import logging as log

CATALOG_API_URL: str = 'https://catalog.api.2gis.com'
PLACES_API_ENDPOINT: str = '/3.0/items'

class PlaceType(Enum):
  ORG = 'branch'
  ATTRACTION = 'attraction'
  BUILDING = 'building'

  def __str__(self):
    return self.value

# TODO - type for fields param


class tGisApi:
  # ----- Common ------
  def __init__(self, api_key: str) -> None:
    self.api_key = api_key


  def _make_request(self, url: str, params: dict) -> dict:
    """Внутренний метод для выполнения HTTP-запросов к API."""
    log.debug(url)
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()


  def _make_catalog_request(self, endpoint: str, params: dict) -> dict:
    url = f"{CATALOG_API_URL}{endpoint}"
    params['key'] = self.api_key

    return self._make_request(url, params)


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


  def _get_additional_fields_list(self) -> list:
    return [
      'items.flags', 'items.full_address_name', 'items.schedule',
      'items.external_content', 'items.reviews', 'items.attribute_groups'
    ]


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


  def get_place(self, place_id: int, additional_info: bool = False) -> Optional[list]:
    """Получить информацию о месте/заведении по его ID."""
    endpoint = f'{PLACES_API_ENDPOINT}/byid'

    params = {
      'id': place_id,
    }

    if (additional_info):
      params['fields'] = ','.join(self._get_additional_fields_list())

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

  # TODO - add search place by coordinates, radius. When 2gis repair this tools