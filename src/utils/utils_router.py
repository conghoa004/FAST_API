from fastapi import APIRouter
from src.utils.utils_controller import root_page

router = APIRouter()

# GET Root page
router.get("/")(root_page)