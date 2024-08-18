import random

from fastapi import APIRouter

from langchain.schema import HumanMessage, SystemMessage
from langchain.chat_models.gigachat import GigaChat

from ..config import GIGA_CHAT_API_TOKEN

from ..utils.gis_api import GisPoint, main_gis_api

import logging as log


# IMPROVE - make as prompt.yaml with langchain.prompts
base_system_prompt_str : str = '''
  Ты профессиональный гид-экскурсовод, который умеет рассказывать интересные и забавные факты или истории о тех или иных местах.
  Ты это делаешь интересно и с юмором, но обязательно в своих ответах опираешься только на проверенную и достоверную информацию.
  Создавай короткий текст, не больше семи предложений.
  Не говори приветствие.
  Не предлагай посетить это место и не задавай вопросы, просто расскажи о нём интересный или забавный факт.
  В начале текста, задорно укажи, что человек, к которому ты обращаешься, недалеко от этого места - всего в {distance} метрах.
'''

# IMPROVE - enrich it by adding a search engine (Google, Yandex, etc.)
giga_chat = GigaChat(
  credentials=GIGA_CHAT_API_TOKEN,
  verify_ssl_certs=False
)

router = APIRouter()

@router.get("/story/find")
def find_story_about_place(lon: float, lat: float, radius: int):
  q: str = 'Достопримечательности'
  items = main_gis_api.search_geoplaces_by_point(q, GisPoint(lon, lat), radius)

  if (not items):
    return {"content": "В этой зоне не нашлось интересных мест :("}

  item: dict = random.choice(items[:5])
  item_lon: float = item.get('point', '').get('lon', 0)
  item_lat: float = item.get('point', '').get('lat', 0)

  distance: int = main_gis_api.get_distance(GisPoint(lon, lat), GisPoint(item_lon, item_lat))

  place_name: str = item.get('full_name', '')
  since: str = item.get('since', '')
  type: str = item.get('subtype_name', '')

  system_prompt_str = base_system_prompt_str.format(distance=distance)
  system_prompt = SystemMessage(content=system_prompt_str)

  user_prompt_str: str = f'Место: {place_name}. Основано: {since}. Тип: {type}'

  messages = [system_prompt, HumanMessage(content=user_prompt_str)]
  story: str = giga_chat(messages).content

  log.debug("System Prompt: %s", system_prompt_str)
  log.debug("User Prompt: %s", user_prompt_str)
  log.debug("Response: %s", story)

  return {"content": story}


@router.get("/story/place")
def get_story_about_place(q: str, distance: int):
  system_prompt_str = base_system_prompt_str.format(distance=distance)
  system_prompt = SystemMessage(content=system_prompt_str)

  user_prompt_str: str = f'Место: {q}.'

  messages = [system_prompt, HumanMessage(content=user_prompt_str)]
  res = giga_chat(messages).content

  log.debug("System Prompt: %s", system_prompt_str)
  log.debug("User Prompt: %s", user_prompt_str)
  log.debug("Response: %s", res)

  return {"content": res}
