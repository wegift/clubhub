import datetime

import requests


def generate_message(story, subteam_id: str = None):
    pull_requests = story["pull_requests"]
    if pull_requests:
        # We really only need the first pull request
        text = f"<{pull_requests[0]['url']}>"
    else:
        text = "Warning, no pull request found."

    if subteam_id is not None:
        title = f"<!subteam^{subteam_id}> {story['name']} has moved into the In Review column."
    else:
        # Perhaps you do not want to tag a group of users but just have it in slack channel for reference
        title = f"{story['name']} has moved into the In Review column."

    return {
        "attachments": [
            {
                "author_name": "Clubhub Bot",
                "title": title,
                "text": text,
                "color": "#FF0000" if not pull_requests else "#000000",
                "ts": datetime.datetime.now().timestamp(),
            }
        ]
    }


def post_message(webhook: str, json):
    requests.post(webhook, json=json)
