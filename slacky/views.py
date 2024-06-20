import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response

SLACK_WEBHOOK_URL = 'https://hooks.slack.com/services/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'

@api_view(['POST'])
def hello_world(request):
    slack_message = {
        "blocks": [
            {
                "type": "header",
                "text": {
                    "type": "plain_text",
                    "text": "Welcome To the todo app",
                    "emoji": True
                }
            },
            {
                "type": "section",
                "fields": [
                    {
                        "type": "mrkdwn",
                        "text": "*Type:*\nPaid Time Off"
                    },
                    {
                        "type": "mrkdwn",
                        "text": "*Created by:*\n<example.com|Fred Enriquez>"
                    }
                ]
            },
            {
                "type": "section",
                "fields": [
                    {
                        "type": "mrkdwn",
                        "text": "*When:*\nAug 10 - Aug 13"
                    }
                ]
            },
            {
                "type": "actions",
                "elements": [
                    {
                        "type": "button",
                        "text": {
                            "type": "plain_text",
                            "emoji": True,
                            "text": "Approve"
                        },
                        "style": "primary",
                        "value": "click_me_123"
                    },
                    {
                        "type": "button",
                        "text": {
                            "type": "plain_text",
                            "emoji": True,
                            "text": "Reject"
                        },
                        "style": "danger",
                        "value": "click_me_123"
                    }
                ]
            }
        ]
    }

    response = requests.post(SLACK_WEBHOOK_URL, json=slack_message)

    if response.status_code != 200:
        return Response({'error': 'Request to Slack returned an error %s, the response is:\n%s' % (response.status_code, response.text)}, status=response.status_code)

    return Response({'message': 'Notification sent to Slack successfully!'}, status=200)