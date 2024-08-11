import requests
from typing import Optional

CATALOG_API_URL: str = 'https://catalog.api.2gis.com'
DEFAUL_PAGE_SIZE: int = 50

class tGisApi:

  # ----- Common ------
  def __init__(self, api_key: str) -> None:
    self.api_key = api_key

  def _make_request(self, url: str, params: dict) -> dict:
    """Внутренний метод для выполнения HTTP-запросов к API."""
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()

  def _make_catalog_request(self, endpoint: str, params: dict) -> dict:
    url = f"{CATALOG_API_URL}{endpoint}"
    params['key'] = self.api_key
    params['page_size'] = DEFAUL_PAGE_SIZE

    return self._make_request(url, params)


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
  def _get_city_rubrics(self, endpoint: str, params: dict) -> Optional[list]:
    data = self._make_catalog_request(endpoint, params)

    rubrics = data.get('result', {}).get('items', [])
    return rubrics


  def list_city_general_rubrics(self, city_id: int, sub_rubrics: bool = False) -> Optional[list]:
    """Получить список общих рубрик города."""
    endpoint = "/2.0/catalog/rubric/list"

    params = {"region_id": city_id}
    if (sub_rubrics): params['fields'] = 'items.rubrics'

    return self._get_city_rubrics(endpoint, params)


  def list_city_rubrics_by_parent(self, city_id: int, parent_id: int, sub_rubrics: bool = False) -> Optional[list]:
    """Получить список рубрик города по id родительской рубрики."""
    endpoint = "/2.0/catalog/rubric/list"

    params = {
      "region_id": city_id,
      "parent_id": parent_id
    }
    if (sub_rubrics): params['fields'] = 'items.rubrics'

    return self._get_city_rubrics(endpoint, params)


  def search_city_rubrics(self, city_id: int, q: str, sub_rubrics: bool = False) -> Optional[list]:
    """Получить список рубрик города по поисковому запросу."""
    endpoint = "/2.0/catalog/rubric/search"

    params = {
      "region_id": city_id,
      "q": q
    }
    if (sub_rubrics): params['fields'] = 'items.rubrics'

    return self._get_city_rubrics(endpoint, params)


  def get_city_rubric_info(self, city_id: int, rubric_id: int, sub_rubrics: bool = False) -> Optional[dict]:
    """Получить информацию о рубрике города по id рубрики."""
    endpoint = "/2.0/catalog/rubric/get"

    params = {
      "region_id": city_id,
      "id": rubric_id
    }
    if (sub_rubrics): params['fields'] = 'items.rubrics'

    data = self._get_city_rubrics(endpoint, params)
    if (not data): return None

    return data[0]
