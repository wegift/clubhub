Custom integration between Gitlab, Clubhouse and Slack.

To make the connection work you need a minimum of 2 things:
1. Slack incoming webhook - This allows you to tell slack where to post this message when hit by the incoming webhook.
   You can find this by going to api.slack.com and looking under the `Incoming Webhooks` section.
2. Team ID - There is logic where this will only send a message if you pass the correct `group_id` (this is your team id).
   You can find this by opening clubhouse and looking for the characters after `https://app.clubhouse.io/company/team/` 
   
If you're a member of WeGift you can check the prod logs by speaking to either Will or Chris. 

Remember that you need to update the prod env variables if you make any changes locally.