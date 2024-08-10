import requests
from typing import Optional

CATALOG_API_URL: str = 'https://catalog.api.2gis.com'

class tGisApi:
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

    return self._make_request(url, params)


  def get_city_id(self, city: str) -> Optional[int]:
    """Получить ID города по его названию."""
    endpoint = "/2.0/region/search"
    params = {"q": city}

    data = self._make_catalog_request(endpoint, params)

    regions = data.get('result', {}).get('items', [])
    if regions:
      return regions[0].get('id')
    return None
