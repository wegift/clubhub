import logging

import flask
from flask import request

from clubhub import gitlab, actions

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.info('message')

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
