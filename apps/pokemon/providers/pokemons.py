from apps.pokemon.common.dataclasses import Pokemon, Specie
from typing import Optional
import requests

PATH = "https://pokeapi.co/api/v2/pokemon/{parameter}"


def get_pokemon_by_id(pokemon_id: int) -> Optional[Pokemon]:
    return get_pokemon(param=pokemon_id)


def get_pokemon_by_name_provider(name: str) -> Optional[Pokemon]:
    return get_pokemon(param=name)


def get_pokemon(param: [str, int]) -> Optional[Pokemon]:
    path = f"https://pokeapi.co/api/v2/pokemon/{param}"
    request = requests.get(path)
    if request.status_code != 200:
        return None

    data = request.json()

    return transform_dict_to_pokemon_class(data=data)


def transform_dict_to_pokemon_class(data: dict) -> Pokemon:
    specie_data = data["species"]
    specie = None
    if specie_data:
        specie = Specie(name=specie_data["name"], url=specie_data["url"])

    return Pokemon(id=data["id"], name=data["name"], height=data["height"], specie=specie)

