from typing import Union
import random

from fastapi import APIRouter

from ..utils.gis_api import main_gis_api, GisPoint

import logging as log

router = APIRouter()


@router.get("/")
def get_root():
  log.debug('get_root')

  items = main_gis_api.search_geoplaces_by_point('достопримечательность', GisPoint(82.89782317789228, 54.97763635724782), 2000)
  item = random.choice(items)

  return {"root": "mock", "item": item}

@router.get("/hello")
def get_hello():
  log.debug('get_hello')
  return {"Hello": "World"}


@router.get("/hello/{some}")
def get_hello_params(some: str, q: Union[str, None] = None):
  log.debug('get_hello_params')
  return {"some": some, "q": q}
