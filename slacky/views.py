from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['POST'])
def hello_world(request):
    print(request.data)
    return Response({
	"blocks": [
		{
			"type": "header",
			"text": {
				"type": "plain_text",
				"text": "New request",
				"emoji": true
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
						"emoji": true,
						"text": "Approve"
					},
					"style": "primary",
					"value": "click_me_123"
				},
				{
					"type": "button",
					"text": {
						"type": "plain_text",
						"emoji": true,
						"text": "Reject"
					},
					"style": "danger",
					"value": "click_me_123"
				}
			]
		}
	]
})
