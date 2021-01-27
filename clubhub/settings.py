import re

from decouple import config, Csv

# Optional Sentry DSN, provide to enable sentry logging
SENTRY_DSN = config("SENTRY_DSN", default=None)

# Label IDs for QA and Code Review labels
CLUBHOUSE_LABEL_ID_CODE_REVIEW = config("CLUBHOUSE_LABEL_ID_CODE_REVIEW")
CLUBHOUSE_LABEL_ID_QA = config("CLUBHOUSE_LABEL_ID_QA")

# Comma separated list of GitLab usernames for Code Review and QA groups
PEOPLE_CODE_REVIEW = config("PEOPLE_CODE_REVIEW", cast=Csv())
PEOPLE_QA = config("PEOPLE_QA", cast=Csv())

STORY_ID_PATTERN = re.compile(config("STORY_ID_PATTERN", "/ch(\d+)/"))
