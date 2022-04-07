from flask import Blueprint, jsonify, request, Response
from apps.pokemon.services.pokemon_services import get_pokemon_by_random_id, get_pokemon_by_name

pokemon_api = Blueprint('pokemon', __name__,
                        template_folder='templates')


def bad_request_exception(message: str, status_code: int = 422) -> Response:
    response = jsonify({"message": message})
    response.status_code = status_code
    return response


@pokemon_api.route('/random/', methods=['POST'])
def pokemon_random():
    if not request.data:
        return bad_request_exception(message="You should include first value and last value")
    else:
        body = request.json
        first_value = body.get("first_value", None)
        last_value = body.get("last_value", None)

    if not isinstance(first_value, int) or not isinstance(last_value, int):
        return bad_request_exception(message="You should include first value and last value")

    status_code, pokemon = get_pokemon_by_random_id(first_value=first_value, last_value=last_value)

    if status_code == 422:
        return bad_request_exception(message="Range values should be correct")

    if status_code == 404:
        return bad_request_exception(message="Pokemon not found", status_code=404)

    response = jsonify(pokemon)
    response.status_code = status_code

    return response


@pokemon_api.route('/name/<name>', methods=['GET'])
def pokemon_by_name(name: str):
    status_code, pokemon = get_pokemon_by_name(name=name)

    if status_code == 404:
        return bad_request_exception(message="Pokemon not found", status_code=404)

    response = jsonify(pokemon)
    response.status_code = status_code

    return response
