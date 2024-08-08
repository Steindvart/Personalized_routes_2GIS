from app.api.api import router
from app.config import app


app.include_router(router, prefix="/api")
