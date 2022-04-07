import pytest

from apps.pokemon.providers.pokemons import get_pokemon_by_id, get_pokemon_by_name_provider, transform_dict_to_pokemon_class
from apps.pokemon.common.dataclasses import Pokemon, Specie


@pytest.mark.parametrize(
    "pokemon_id",
    [1, 2, 3]
)
def test_get_pokemon_by_id(pokemon_id):
    pokemon = get_pokemon_by_id(pokemon_id=pokemon_id)
    assert pokemon is not None
    assert pokemon.id == pokemon_id


@pytest.mark.parametrize(
    "pokemon_id",
    [111111, 2222222, 3333333]
)
def test_get_pokemon_by_id_doesnt_exists(pokemon_id):
    pokemon = get_pokemon_by_id(pokemon_id=pokemon_id)
    assert pokemon is None


@pytest.mark.parametrize(
    "name",
    ["ditto", "pikachu", "charizard"]
)
def test_get_pokemon_by_name(name):
    pokemon = get_pokemon_by_name_provider(name=name)
    assert pokemon is not None
    assert pokemon.name == name


@pytest.mark.parametrize(
    "name",
    ["dittto", "pikkachu", "cccharizard"]
)
def test_get_pokemon_by_name_doesnt_exists(name):
    pokemon = get_pokemon_by_name_provider(name=name)
    assert pokemon is None


def test_transform_dict_to_pokemon_class():
    data = {
        "id": 1,
        "name": "ditto",
        "height": 7,
        "species": {
            "name": "Normal",
            "url": "www.google.com"
        }
    }
    pokemon = transform_dict_to_pokemon_class(data=data)
    assert isinstance(pokemon, Pokemon)
    assert isinstance(pokemon.specie, Specie)
    assert pokemon.id == data.get("id")
    assert pokemon.name == data.get("name")
