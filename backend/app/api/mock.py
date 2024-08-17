from typing import Union

from fastapi import APIRouter

from ..utils.gis_api import main_gis_api, GisPoint

import logging as log

router = APIRouter()


@router.get("/")
def get_root():
  log.debug('get_root')

  item = main_gis_api.get_place_all_info('70000001030552091', True)
  addr_cooment = item.get('address_comment', '')
  gen_rating = item.get('reviews', '').get('general_rating', 0)

  return {"root": "mock", "item": item, "com": addr_cooment, "rating": gen_rating}

@router.get("/hello")
def get_hello():
  log.debug('get_hello')
  return {"Hello": "World"}


@router.get("/hello/{some}")
def get_hello_params(some: str, q: Union[str, None] = None):
  log.debug('get_hello_params')
  return {"some": some, "q": q}
