from apps.hello_world.common.dataclasses import Greeting


def greeting(name: str = None) -> Greeting:
    message = "Hello, world"
    code = 200
    if name is not None and isinstance(name, str):
        message = f"Hello, {name}"
        code = 200

    if name is not None and not isinstance(name, str):
        message = "Invalid parameter"
        code = 422

    return Greeting(message=message, code=code)
