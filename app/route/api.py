from fastapi import APIRouter
from app.endpoint import status, python_scripts

router = APIRouter()
router.include_router(status.router)
router.include_router(python_scripts.router)