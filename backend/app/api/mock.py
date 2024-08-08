from typing import Union

from fastapi import APIRouter

api_router = APIRouter()


@api_router.get("/hello")
def read_root():
  return {"Hello": "World"}


@api_router.get("/hello/{some}")
def read_item(some: str, q: Union[str, None] = None):
  return {"some": some, "q": q}
