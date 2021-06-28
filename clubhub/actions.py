import logging

from clubhub import clubhouse, gitlab, settings, slack

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


def on_clubhouse_event(event):
    if clubhouse.is_update_event(event):
        if clubhouse.moved_between_columns(
            event, clubhouse.IN_REVIEW_COLUMN, clubhouse.IN_DEVELOPMENT_COLUMN
        ):
            event_id = event["actions"][0]["id"]
            log.info("%s is an update event", event_id)
            story = clubhouse.client.getStory(event_id)
            # TODO - Currently this is only for distibution team, it should be expanded to be configurable for any team
            if story["group_id"] == settings.DISTRIBUTION_TEAM_USER_GROUP_ID_CLUBHOUSE:
                message = slack.generate_message(story)
                log.info("Message generated %s", message)
                slack.post_message(
                    webhook=settings.DISTRIBUTION_TEAM_SLACK_WEBHOOK, json=message
                )
            else:
                log.info(
                    "Event %s is not for the growth team, not pushing message",
                    event["id"],
                )
        else:
            log.info(
                "Event %s has not moved from In Development to In Review. Not pushing message",
                event["id"],
            )

    else:
        log.info("Event %s is not an update event, not pushing message", event["id"])
