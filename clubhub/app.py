import logging

import flask
import sentry_sdk
from flask import request
from sentry_sdk.integrations.flask import FlaskIntegration

from clubhub import actions, gitlab, settings

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.info("Booting clubhub")

if settings.SENTRY_DSN:
    logger.info("Init Sentry")
    sentry_sdk.init(dsn=settings.SENTRY_DSN, integrations=[FlaskIntegration()])

app = flask.Flask(__name__)


@app.route("/")
def hello_world():
    return "<h1>clubhub</h1><p>Hello World</p>"


@app.route("/gitlab-webhook", methods=["POST"])
def gitlab_webhook():
    # return jsonify(request.json)
    event = gitlab.GitlabEvent.from_json(request.json)
    actions.on_gitlab_event(event)
    return {}
    # return jsonify(event)


@app.route("/exc")
def raise_exception():
    raise Exception("Test exception")


@app.route("/clubhouse-webhook", methods=["POST"])
def clubhouse_webhook():
    event = request.json  # Event from clubhouse webhook
    # It's possible to get empty events via the webhook for some reason
    if event is not None:
        logger.info("Actioning %s", event["id"])
        actions.on_clubhouse_event(event)
    return {}
