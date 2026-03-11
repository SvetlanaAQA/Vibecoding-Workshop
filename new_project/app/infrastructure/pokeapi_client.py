import httpx
import random
from typing import List
from fastapi import HTTPException

class PokeAPIClient:
    BASE_URL = "https://pokeapi.co/api/v2/pokemon"

    async def get_all_names(self) -> List[str]:
        # Fetching a large batch (up to 1000) to select randomly from
        async with httpx.AsyncClient() as client:
            try:
                response = await client.get(f"{self.BASE_URL}?limit=1000")
                response.raise_for_status()
                data = response.json()
                return [p["name"] for p in data["results"]]
            except httpx.HTTPError:
                raise HTTPException(status_code=502, detail="External API (PokeAPI) error")
