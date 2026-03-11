from fastapi import APIRouter
from app.api.v1.endpoints import health, info, calculator, pokemon

api_router = APIRouter()
api_router.include_router(health.router, prefix="/health", tags=["System"])
api_router.include_router(info.router, prefix="/info", tags=["User"])
api_router.include_router(calculator.router, prefix="/calculator", tags=["Calculator"])
api_router.include_router(pokemon.router, prefix="/pokemon", tags=["Pokemon"])
