from fastapi import APIRouter
from src.user.user_controller import index

router = APIRouter()

# GET info user
router.get("/users")(index)