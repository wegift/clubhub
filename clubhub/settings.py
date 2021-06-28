import re

from decouple import Csv, config

# Optional Sentry DSN, provide to enable sentry logging
SENTRY_DSN = config("SENTRY_DSN", default=None)

# Label IDs for QA and Code Review labels
CLUBHOUSE_LABEL_ID_CODE_REVIEW = config("CLUBHOUSE_LABEL_ID_CODE_REVIEW")
CLUBHOUSE_LABEL_ID_QA = config("CLUBHOUSE_LABEL_ID_QA")

# Comma separated list of GitLab usernames for Code Review and QA groups
PEOPLE_CODE_REVIEW = config("PEOPLE_CODE_REVIEW", cast=Csv())
PEOPLE_QA = config("PEOPLE_QA", cast=Csv())

STORY_ID_PATTERN = re.compile(config("STORY_ID_PATTERN", "/ch(\d+)/"))

# Slack User Group ID
DISTRIBUTION_TEAM_USER_GROUP_ID_CLUBHOUSE = config(
    "DISTRIBUTION_TEAM_USER_GROUP_ID_CLUBHOUSE"
)
DISTRIBUTION_SUBTEAM_ID_SLACK = config("DISTRIBUTION_SUBTEAM_ID_SLACK")
DISTRIBUTION_TEAM_SLACK_WEBHOOK = config("DISTRIBUTION_TEAM_SLACK_WEBHOOK")
