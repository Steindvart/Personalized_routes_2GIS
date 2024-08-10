from fastapi import FastAPI

from environs import Env

env = Env()
env.read_env()

import logging as log

# NOTE - configure immediately after logging import is IMPORTANT!
log.basicConfig(filename='app.log',
                level=log._nameToLevel['DEBUG'],
                format='[{asctime}] {levelname:8} {filename}: {lineno} - {name} - {message}',
                style='{',
                encoding='utf-8'
)

GIGA_CHAT_API_TOKEN = env('GIGA_CHAT_API_TOKEN')

app = FastAPI()
