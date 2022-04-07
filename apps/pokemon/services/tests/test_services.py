import pytest


from apps.pokemon.services.pokemon_services import get_pokemon_by_random_id, get_pokemon_by_name


@pytest.mark.parametrize([
    "first_value", "last_value"
], [
    [1, 5],
    [1, 10],
    [11, 25],
    [26, 50],
])
def test_get_pokemon_by_random_id(first_value, last_value):
    status_code, pokemon = get_pokemon_by_random_id(first_value=first_value, last_value=last_value)
    assert status_code == 200
    assert pokemon is not None
    assert first_value <= pokemon.id <= last_value


@pytest.mark.parametrize([
    "first_value", "last_value"
], [
    [1111111, 55555555],
    [1111111, 10000000],
    [1111111, 25252525],
    [2626262, 505050505],
])
def test_get_pokemon_by_random_id(first_value, last_value):
    status_code, pokemon = get_pokemon_by_random_id(first_value=first_value, last_value=last_value)
    assert status_code == 404
    assert pokemon is None


@pytest.mark.parametrize(
    "name",
    ["ditto", "pikachu", "charizard"]
)
def test_get_pokemon_by_name(name):
    status_code, pokemon = get_pokemon_by_name(name=name)

    assert status_code == 200
    assert pokemon is not None
    assert pokemon.name == name


@pytest.mark.parametrize(
    "name",
    ["dittto", "pikkachu", "cccharizard"]
)
def test_get_pokemon_by_name_doesnt_exists(name):
    status_code, pokemon = get_pokemon_by_name(name=name)
    assert status_code == 404
    assert pokemon is None
