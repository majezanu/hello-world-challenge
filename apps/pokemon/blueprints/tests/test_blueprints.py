import pytest


@pytest.mark.parametrize([
    "first_value", "last_value", "expected_code"
], [
    [1, 5, 200],
    [6, 10, 200],
    [20, 80, 200],
    [80, 100, 200],
    [111111, 222222, 404],
    [555555, 999999, 404],
    ["12", "14", 422],
    ["ABC", "DFE", 422],
    [2, 1, 422],
    [10, 8, 422],
    [-3, -1, 422],
])
def test_get_pokemon_by_random_id(client, first_value, last_value, expected_code):
    path = f"/pokemon/random/"
    response = client.post(path, json={"first_value": first_value, "last_value": last_value})
    assert response.status_code == expected_code


@pytest.mark.parametrize(
    [
        "name", "expected_code"
    ],
    [
        ["ditto", 200],
        ["pikachu", 200],
        ["Pikkachu", 404],
    ]
)
def test_get_pokemon_by_name(client, name, expected_code):
    path = f"/pokemon/name/{name}"
    response = client.get(path)
    assert response.status_code == expected_code
