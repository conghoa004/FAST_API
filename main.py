from typing import Union
from fastapi import FastAPI
from src.user.user_router import router as user_router
from src.utils.utils_router import router as utils_router

# Create the app
app = FastAPI()

# Include routers
app.include_router(utils_router)
app.include_router(user_router)