from app.api.routes import router as api_router

from app.exceptions.handlers import (
    not_found_exception_handler,
    bad_request_exception_handler,
    generic_exception_handler,
    NotFoundException,
    BadRequestException,
)

from app.config import app

import logging as log

log.debug('app run')
app.include_router(api_router, prefix="/api")

exception_handlers = {
    NotFoundException: not_found_exception_handler,
    BadRequestException: bad_request_exception_handler,
    Exception: generic_exception_handler,
}

for exc, handler in exception_handlers.items():
    app.add_exception_handler(exc, handler)
