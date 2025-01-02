from fastapi import APIRouter
from api.routes import test
router = APIRouter()
router.include_router(test.router, tags=["test"])

