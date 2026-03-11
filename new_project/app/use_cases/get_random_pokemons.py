from typing import List
import random
from app.infrastructure.pokeapi_client import PokeAPIClient

class GetRandomPokemons:
    def __init__(self, client: PokeAPIClient = None):
        self.client = client or PokeAPIClient()

    async def execute(self, count: int = 5) -> List[str]:
        all_names = await self.client.get_all_names()
        # Ensure we don't try to pick more than we have
        actual_count = min(count, len(all_names))
        return random.sample(all_names, actual_count)
