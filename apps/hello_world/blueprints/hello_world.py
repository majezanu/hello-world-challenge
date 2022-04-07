from flask import Blueprint, jsonify, request
from apps.hello_world.services import greeting_services

hello_world = Blueprint('hello-world', __name__,
                        template_folder='templates')


@hello_world.route('/greeting/', methods=['POST', 'GET'])
@hello_world.route('/greeting/<name>', methods=['GET'])
def show(name: str = None):
    if request.method == "GET":
        name = request.view_args.get("name", None)

    if request.method == "POST" and request.data:
        body = request.json
        name = body.get("name", None)

    greeting = greeting_services.greeting(name)
    response = jsonify(greeting)
    response.status_code = greeting.code
    return response
