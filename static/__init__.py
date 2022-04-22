from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
import logging

from static.logger_config import custom_logger


db = SQLAlchemy()
migrate = Migrate()

logger = logging.getLogger('static')
logger = custom_logger(logger)


def create_app(test_config=None):
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://kqpkycwfgertsv:89979389d84a2f3940e884b306e2ba5f352392c54a03d80cc7e52e811242510c@ec2-3-224-125-117.compute-1.amazonaws.com:5432/d46sihl33mklvo'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    from static.todoApp.model.todo_list_model import Todo
    db.init_app(app)
    migrate.init_app(app, db)

    from static.todoApp import todo_list
    app.register_blueprint(todo_list, url_prefix="/api/v1")

    return app
