import uvicorn

from app.api.routes import router as api_router
from app.config import app

import logging as log

log.debug('app run')
app.include_router(api_router, prefix="/api")


if __name__ == "__main__":
  uvicorn.run(app, host="127.0.0.1", port=8000)