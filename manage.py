from flask.cli import FlaskGroup
from todoapp import app


cli = FlaskGroup(app)


if __name__ == "__main__":
    cli()
