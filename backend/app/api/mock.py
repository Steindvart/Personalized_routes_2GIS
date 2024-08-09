from typing import Union

from fastapi import APIRouter

import logging as log

router = APIRouter()


@router.get("/")
def get_root():
  log.debug('get_root')
  return {"root": "mock"}

@router.get("/hello")
def get_hello():
  log.debug('get_hello')
  return {"Hello": "World"}


@router.get("/hello/{some}")
def get_hello_params(some: str, q: Union[str, None] = None):
  log.debug('get_hello_params')
  return {"some": some, "q": q}
