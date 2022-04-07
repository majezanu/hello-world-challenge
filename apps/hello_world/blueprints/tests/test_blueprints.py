import pytest


@pytest.mark.parametrize(
    [
        "name", "expected_code", "expected_message"
    ],
    [
        ["Manuel", 200, "Hello, Manuel"],
        [None, 200, "Hello, world"],
        ["Zavala", 200, "Hello, Zavala"],
        [True, 200, "Hello, True"],
        [False, 200, "Hello, False"],
        [1, 200, "Hello, 1"],
    ]
)
def test_greeting_with_get_method(client, name, expected_code, expected_message):
    path = f"/hello-world/greeting/{name}" if name is not None else "/hello-world/greeting/"
    response = client.get(path)
    assert response.json == {"code": expected_code, "message": expected_message}


@pytest.mark.parametrize(
    [
        "name", "expected_code", "expected_message"
    ],
    [
        ["Manuel", 200, "Hello, Manuel"],
        [None, 200, "Hello, world"],
        ["Zavala", 200, "Hello, Zavala"],
        [True, 422, "Invalid parameter"],
        [False, 422, "Invalid parameter"],
        [1, 422, "Invalid parameter"],
    ]
)
def test_greeting_with_post_method(client, name, expected_code, expected_message):
    path = "/hello-world/greeting/"
    response = client.post(path, json={"name": name}) if name is not None else client.post(path)
    assert response.json == {"code": expected_code, "message": expected_message}
