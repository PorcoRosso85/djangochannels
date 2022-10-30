import json
from channels.generic.websocket import WebsocketConsumer

class ChatConsumer(WebsocketConsumer):

    def connect(self):
        # self.room_name = room_name
        self.accept()

    def disconnect(self):
        pass

    def receive(self, text_data):
        message = json.loads(text_data)['message']
        self.send(
            text_data = json.dumps({
                'message': message
            })
        )
