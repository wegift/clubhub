import logging

from clubhub import clubhouse, gitlab, settings

log = logging.getLogger(__name__)


def on_gitlab_event(event: gitlab.GitlabEvent):
    log.info(
        "Processing gitlab event %s / %s / %s",
        event.username,
        event.event_type,
        event.action,
    )
    if event.event_type == gitlab.EVENT_TYPE_MR and event.action in {
        gitlab.ACTION_MR_APPROVE,
        gitlab.ACTION_MR_APPROVAL,
    }:
        # Is approval
        on_gitlab_mr_approve(event)
    else:
        log.info("No action to take")


def on_gitlab_mr_approve(event: gitlab.GitlabEvent):
    story_id = clubhouse.get_story_id_from_branch_name(event.source_branch)

    if not story_id:
        log.info("No story ID for approve event on branch %s", event.source_branch)
        return

    log.info("Matched story id %d for branch %s", story_id, event.source_branch)

    if event.username in settings.PEOPLE_CODE_REVIEW:
        log.info(
            "Adding code review label to story %d from branch %s",
            story_id,
            event.source_branch,
        )
        clubhouse.add_label_to_story(story_id, settings.CLUBHOUSE_LABEL_ID_CODE_REVIEW)
    elif event.username in settings.PEOPLE_QA:
        log.info(
            "Adding qa label to story %d from branch %s", story_id, event.source_branch
        )
        clubhouse.add_label_to_story(story_id, settings.CLUBHOUSE_LABEL_ID_QA)
    else:
        log.info("User %s not in any list, not adding label", event.username)
