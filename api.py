from flask import Flask


def create_app(config_filename: str = None):
    app = Flask(__name__)

    app.config.from_object(config_filename)

    from apps.hello_world.blueprints.hello_world import hello_world as hello_world_blueprint
    from apps.pokemon.blueprints.pokemon_api import pokemon_api as pokemon_api_blueprint
    app.register_blueprint(hello_world_blueprint, url_prefix="/hello-world")
    app.register_blueprint(pokemon_api_blueprint, url_prefix="/pokemon")

    return app


if __name__ == "__main__":
    api = create_app()
    api.run()
