from app.api.routes import router as api_router
from config import app

import logging as log

log.debug('app run')
app.include_router(api_router, prefix="/api")
