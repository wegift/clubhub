import logging
from os import environ

import flask
import sentry_sdk
from flask import request
from sentry_sdk.integrations.flask import FlaskIntegration

from clubhub import gitlab, actions

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.info('Booting clubhub')

if environ.get('SENTRY_DSN'):
    logger.info('Init Sentry')
    sentry_sdk.init(
        dsn=environ.get('SENTRY_DSN'),
        integrations=[FlaskIntegration()]
    )

app = flask.Flask(__name__)


@app.route('/')
def hello_world():
    return "<h1>clubhub</h1><p>Hello World</p>"


@app.route('/gitlab-webhook', methods=['POST'])
def gitlab_webhook():
    # return jsonify(request.json)
    event = gitlab.GitlabEvent.from_json(request.json)
    actions.on_gitlab_event(event)
    return {}
    # return jsonify(event)


@app.route('/exc')
def raise_exception():
    raise Exception("Test exception")
