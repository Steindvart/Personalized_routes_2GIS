from fastapi import FastAPI

from environs import Env

from dotenv import load_dotenv
import os

import logging as log

env = Env()
env.read_env()

# NOTE - configure immediately after logging import is IMPORTANT!
log.basicConfig(filename='app.log',
                level=log._nameToLevel['DEBUG'],
                format='[{asctime}] {levelname:8} {filename}: {lineno} - {name} - {message}',
                style='{',
                encoding='utf-8'
)

GIGA_CHAT_API_TOKEN = env('GIGA_CHAT_API_TOKEN')

app = FastAPI()

load_dotenv()

DB_HOST = os.environ.get("DB_HOST")
DB_PORT = os.environ.get("DB_PORT")
DB_NAME = os.environ.get("DB_NAME")
DB_USER = os.environ.get("DB_USER")
DB_PASS = os.environ.get("DB_PASS")
