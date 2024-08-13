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

T_GIS_API_KEY = env('T_GIS_API_KEY')
GIGA_CHAT_API_TOKEN = env('GIGA_CHAT_API_TOKEN')

app = FastAPI()

DB_HOST = env("DB_HOST")
DB_PORT = env("DB_PORT")
DB_NAME = env("DB_NAME")
DB_USER = env("DB_USER")
DB_PASS = env("DB_PASS")
