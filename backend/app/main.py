from config import app
from api.api import api_router


app.include_router(api_router, prefix="/api")