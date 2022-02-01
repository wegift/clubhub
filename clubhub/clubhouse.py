from os import environ

from requests import HTTPError

import clubhouse_lib
from clubhouse_lib.type import CreateLabelParams, Label
from clubhub import settings

client = clubhouse_lib.ClubhouseClient(environ.get("CLUBHOUSE_API_TOKEN"))

IN_REVIEW_COLUMN = "In Review"
IN_DEVELOPMENT_COLUMN = "In Development"


def get_story_id_from_branch_name(branch_name: str):
    match = settings.STORY_ID_PATTERN.search(f"{branch_name}")
    return int(match[1]) if match else None


def label_to_create_params(label: Label) -> CreateLabelParams:
    return {
        "color": label["color"],
        "description": label["description"],
        "external_id": label["external_id"] or str(label["id"]),
        "name": label["name"],
    }


def add_label_to_story(story_id, label_id):
    new_label = label_to_create_params(client.getLabel(label_id))
    story = client.getStory(story_id)
    existing_labels = [label_to_create_params(l) for l in story["labels"]]
    try:
        client.updateStory(story_id, labels=[*existing_labels, new_label])
    except HTTPError as e:
        print(e.response.json())


def is_update_event(event) -> bool:
    # TODO - Should be a function which checks for event type passed. Currently specific to growth team
    if event["actions"]:
        if len(event["actions"]) == 1:
            return event["actions"][0]["action"] == "update"


def moved_between_columns(event, to_column, from_column) -> bool:
    # Length of references should be at least 2
    if "references" in event and len(event["references"]) >= 2:
        return (
            event["references"][0]["name"] == to_column
            and event["references"][1]["name"] == from_column
        )


# print(client.getStory(3984)['labels'])
# add_label_to_story(3984, CLUBHOUSE_LABEL_ID_CODE_REVIEW)
# print(get_story_id_from_branch_name("ch123/hello"))
