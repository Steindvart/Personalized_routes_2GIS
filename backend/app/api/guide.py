from fastapi import APIRouter

from langchain.schema import HumanMessage, SystemMessage
from langchain.chat_models.gigachat import GigaChat

from ..config import GIGA_CHAT_API_TOKEN

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
