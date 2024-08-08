from typing import Union

from fastapi import APIRouter

router = APIRouter()


@router.get("/hello")
def read_root():
  return {"Hello": "World"}


@router.get("/hello/{some}")
def read_item(some: str, q: Union[str, None] = None):
  return {"some": some, "q": q}