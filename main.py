from typing import Union
from fastapi import FastAPI
from routers.user import router as user_router
from routers.utils import router as utils_router

# Create the app
app = FastAPI()

# Include routers
app.include_router(user_router)
app.include_router(utils_router)