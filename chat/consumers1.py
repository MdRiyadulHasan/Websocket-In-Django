from channels.consumer import SyncConsumer, AsyncConsumer
from channels.exceptions import StopConsumer
from time import sleep
import asyncio
import json
from asgiref.sync import async_to_sync

class MySyncConsumer(SyncConsumer):
    def websocket_connect(self, event):
        print("connected .....", event)

        print("Channel Layer ..", self.channel_layer)
        print("Channel Name ..", self.channel_name)
        async_to_sync (self.channel_layer.group_add)(
            "programmers", self.channel_name
        )
        self.send({
            'type':'websocket.accept',
        })

    def websocket_receive(self, event):
        print("receiving .....", event['text'])
        async_to_sync (self.channel_layer.group_send)(
            'programmers', 
            {
                'type':'chat.message',
                'message': event['text']
            }
        )
    def chat_message(self, event):
        print("Event .. ",event)
        print('Actual Data .. ', event['message'])
        self.send({
            'type':'websocket.send',
            'text': event['message'],
        })

    def websocket_disconnect(self, event):
        print("Channel Layer ..", self.channel_layer)

        print("Channel Name ..", self.channel_name)

        async_to_sync (self.channel_layer.group_discard)(
            "programmers", self.channel_name
        )

        print("disconnected .....", event)
        raise StopConsumer()


# class MyASyncConsumer(AsyncConsumer):
#     async def websocket_connect(self, event):
#         print("connected .....", event)
#         await self.send({
#             'type':'websocket.accept',
#         })

#     async def websocket_receive(self, event):
#         print("receiving .....", event)
#         print("message", event['text'])

#         for i in range(10):
#             await self.send({
#                 'type':'websocket.send',
#                 'text':json.dumps({"count":i})
#             })
#             asyncio.sleep(1)
            
#     async def websocket_disconnect(self, event):
#         print("disconnected .....", event)
#         raise StopConsumer()
class MyASyncConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        print("connected .....", event)

        print("Channel Layer ..", self.channel_layer)
        print("Channel Name ..", self.channel_name)
        # groupName1 = self.scope['url_route']['kwargs']['groupname1']
        self.groupName = self.scope['url_route']['kwargs']['groupname']

        print("group Name ",self.groupName ) 



        await self.channel_layer.group_add(
            self.groupName, self.channel_name
        )
        await self.send({
            'type':'websocket.accept',
        })

    async def websocket_receive(self, event):
        print("receiving .....", event['text'])
        await self.channel_layer.group_send(
            self.groupName, 
            {
                'type':'chat.message',
                'message': event['text']
            }
        )
    async def chat_message(self, event):
        print("Event .. ",event)
        print('Actual Data .. ', event['message'])
        await self.send({
            'type':'websocket.send',
            'text': event['message'],
        })

    async def websocket_disconnect(self, event):
        print("Channel Layer ..", self.channel_layer)

        print("Channel Name ..", self.channel_name)

        await self.channel_layer.group_discard(
            self.groupName, self.channel_name
        )

        print("disconnected .....", event)
        raise StopConsumer()