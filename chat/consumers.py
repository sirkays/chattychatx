# chat/consumers.py
import json
from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import Chat,ChatBoxData
from django.utils import timezone

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        message_user = text_data_json['message_user']

        # Find ChatBox
        chat_box = await database_sync_to_async(ChatBoxData.objects.get)(room=self.room_name)

        #Create New Chat
        chat = Chat(chat_box=chat_box,message=message,user=message_user)
        
        await database_sync_to_async(chat.save)()
        timestamp = chat.timestamp
        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'message_user':message_user,
                'timestamp':timestamp
            }
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']
        message_user = event['message_user']
        timestamp = event['timestamp']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            'message_user':message_user,
            'timestamp':timestamp
            
        }))
