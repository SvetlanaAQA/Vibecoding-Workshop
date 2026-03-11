from fastapi import APIRouter, Query
from typing import List
from app.use_cases.get_random_pokemons import GetRandomPokemons

router = APIRouter()

@router.get("/random", response_model=List[str])
async def get_random_pokemons(
    count: int = Query(default=5, le=20, ge=1, description="Number of random pokemon to fetch")
):
    use_case = GetRandomPokemons()
    return await use_case.execute(count)
