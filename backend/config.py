from fastapi import FastAPI

import logging as log

# NOTE - configure immediately after logging import is IMPORTANT!
log.basicConfig(filename='app.log',
                level=log._nameToLevel['DEBUG'],
                format='[{asctime}] {levelname:8} {filename}: {lineno} - {name} - {message}',
                style='{'
)

app = FastAPI()
