import os
from flask import Flask
from modules.exceptions import InvalidInputParameter


PROD = "PRODUCTION"
DEV = "DEVELOPMENT"
STAGING = "STAGING"
AVAILABLE_ENVIRONMENTS = [PROD, DEV, STAGING]


def load_config(app, env):
    app.config["ENVIRONMENT"] = env
    global_config_path = os.path.join(app.root_path, "config/default.py")
    app.config.from_pyfile(global_config_path)

    env_config_path = os.path.join(app.root_path, f"config/{env.lower()}.py")
    app.config.from_pyfile(env_config_path)


def register_blueprints(app):
    from modules.views.main_blueprint import main_bp
    app.register_blueprint(main_bp)

    from modules.views.base_blueprint import base_bp
    app.register_blueprint(base_bp)


def create_app(env: str):
    if env not in AVAILABLE_ENVIRONMENTS:
        raise InvalidInputParameter(f"Invalid value for env={env}")

    app = Flask(__name__)
    load_config(app, env)

    register_blueprints(app)

    print("#" * 50, f"{' ' * 10} * Environment: {env}", "#" * 50, sep='\n')

    return app



if __name__ == "__main__":
    env_name = os.getenv('FLASK_ENVIRONMENT', 'DEVELOPMENT')
    app = create_app(env_name)
    app.run(port=5000, debug=True)
