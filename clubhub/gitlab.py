from dataclasses import dataclass

# Event types
from typing import Dict

EVENT_TYPE_MR = "merge_request"

# Actions
ACTION_MR_OPEN = "open"
# For some reason there are two actions for approval, unsure why
ACTION_MR_APPROVE = "approved"
ACTION_MR_APPROVAL = "approval"


@dataclass(frozen=True)
class GitlabEvent:
    event_type: str
    action: str
    # Branch
    source_branch: str
    # User
    avatar_url: str
    email: str
    name: str
    username: str

    @classmethod
    def from_json(cls, json: Dict) -> "GitlabEvent":
        return cls(
            event_type=json.get("event_type"),
            action=json.get("object_attributes", {}).get("action"),
            source_branch=json.get("object_attributes", {}).get("source_branch"),
            avatar_url=json.get("user", {}).get("avatar_url"),
            email=json.get("user", {}).get("email"),
            name=json.get("user", {}).get("name"),
            username=json.get("user", {}).get("username"),
        )
