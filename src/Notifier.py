import json
import os
import requests


### Notify slack channel
class Notifier:

    def __init__(self, slack_url=os.environ['SLACK_URL']) -> None:
        self.slack_url = slack_url

    def construct_payload(self, items):
        payload = {"text": "The challenges for this week are attached below"}

        payload['attachments'] = []

        for item in items:
            payload['attachments'].append({
                "title":
                item.get('title', "No title"),
                'image_url':
                item.get('description', "https://leetcode.com/problems")
            })

        return payload

    def post(self, items, channel=None):
        payload = self.construct_payload(items)

        # payload['channel'] = "weekly-challenges" if channel is None else channel
        payload['username'] = "Leetcode Weekly challenge"
        print(json.dumps(payload))

        res = requests.post(self.slack_url,
                            data=json.dumps(payload),
                            headers={'Content-type': 'application/json'})
        # res.raise_for_status()

        print(res.text)

        return True