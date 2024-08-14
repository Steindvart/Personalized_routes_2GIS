from app.api.routes import router as api_router

from app.exceptions.handlers import not_found_exception_handler
from app.exceptions.handlers import bad_request_exception_handler
from app.exceptions.handlers import generic_exception_handler
from app.exceptions.handlers import NotFoundException
from app.exceptions.handlers import BadRequestException

from app.config import app

import logging as log

log.debug('app run')
app.include_router(api_router, prefix="/api")

app.add_exception_handler(NotFoundException, not_found_exception_handler)
app.add_exception_handler(BadRequestException, bad_request_exception_handler)
app.add_exception_handler(Exception, generic_exception_handler)
