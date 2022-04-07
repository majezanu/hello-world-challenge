import pytest

from apps.hello_world.services.greeting_services import greeting
from apps.hello_world.common.dataclasses import Greeting


@pytest.mark.parametrize(
    [
        "name", "expected_code", "expected_message"
    ],
    [
        ["Manuel", 200,  "Hello, Manuel"],
        [None, 200, "Hello, world"],
        ["Zavala", 200, "Hello, Zavala"],
        [True, 422, "Invalid parameter"],
        [False, 422, "Invalid parameter"],
        [1, 422, "Invalid parameter"],
    ]
)
def test_greeting(name, expected_code, expected_message):
    response = greeting(name)
    assert response == Greeting(
        message=expected_message, code=expected_code
    )
    assert isinstance(response, Greeting)
