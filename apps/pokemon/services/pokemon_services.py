import random

from apps.pokemon.providers.pokemons import get_pokemon_by_id, get_pokemon_by_name_provider
from apps.pokemon.common.dataclasses import Pokemon
from typing import Optional


def get_pokemon_by_random_id(first_value: int = 0, last_value: int = 0) -> (int, Optional[Pokemon]):
    if last_value < first_value:
        return 422, None

    if first_value < 0 or last_value < 0:
        return 422, None

    random_id = random.randint(a=first_value, b=last_value)
    pokemon = get_pokemon_by_id(pokemon_id=random_id)
    status_code = 200
    if not pokemon:
        status_code = 404

    return status_code, pokemon


def get_pokemon_by_name(name: str) -> (int, Optional[Pokemon]):
    pokemon = get_pokemon_by_name_provider(name=name)
    status_code = 200
    if not pokemon:
        status_code = 404

    return status_code, pokemon
