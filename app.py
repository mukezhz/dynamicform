from flask import Flask

from api.route.user import user_api as user_api_blueprint
from api.route.form import form_api as form_api_blueprint

app = Flask(__name__)

## Initialize Config
app.config.from_object("config")

app.register_blueprint(user_api_blueprint, url_prefix="/api/users")
app.register_blueprint(form_api_blueprint, url_prefix="/api/forms")


if __name__ == "__main__":
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument(
        "-p", "--port", default=5000, type=int, help="port to listen on"
    )
    args = parser.parse_args()
    port = args.port
    app.run(host="0.0.0.0", port=port)
