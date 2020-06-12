import re
from os import environ

import clubhouse_lib
from clubhouse_lib.type import CreateLabelParams, Label
from requests import HTTPError

CLUBHOUSE_LABEL_ID_QA = int(environ.get("CLUBHOUSE_LABEL_ID_QA"))
CLUBHOUSE_LABEL_ID_CODE_REVIEW = int(environ.get("CLUBHOUSE_LABEL_ID_CODE_REVIEW"))

client = clubhouse_lib.ClubhouseClient(environ.get('CLUBHOUSE_API_TOKEN'))

STORY_ID_PATTERN = re.compile("/ch(\d+)/")


def get_story_id_from_branch_name(branch_name: str):
    match = STORY_ID_PATTERN.search(f"/{branch_name}/")
    return int(match[1]) if match else None


def label_to_create_params(label: Label) -> CreateLabelParams:
    return {
        'color': label['color'],
        'description': label['description'],
        'external_id': label['external_id'] or str(label['id']),
        'name': label['name'],
    }


def add_label_to_story(story_id, label_id):
    new_label = label_to_create_params(client.getLabel(label_id))
    story = client.getStory(story_id)
    existing_labels = [label_to_create_params(l) for l in story['labels']]
    try:
        client.updateStory(story_id, labels=[*existing_labels, new_label])
    except HTTPError as e:
        print(e.response.json())

# print(client.getStory(3984)['labels'])
# add_label_to_story(3984, CLUBHOUSE_LABEL_ID_CODE_REVIEW)
# print(get_story_id_from_branch_name("ch123/hello"))
