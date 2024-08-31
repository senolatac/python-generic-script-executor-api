from fastapi import APIRouter
from app.endpoint import status, executor

router = APIRouter()
router.include_router(status.router)
router.include_router(executor.router)