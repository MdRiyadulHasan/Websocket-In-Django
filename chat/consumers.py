from channels.consumer import SyncConsumer, AsyncConsumer
from channels.exceptions import StopConsumer
from time import sleep
import asyncio

class MySyncConsumer(SyncConsumer):
    def websocket_connect(self, event):
        print("connected .....", event)
        self.send({
            'type':'websocket.accept',
        })

    def websocket_receive(self, event):
        print("receiving .....", event)
        print("message", event['text'])

        for i in range(50):
            self.send({
                'type':'websocket.send',
                'text':str(i)
            })
            sleep(1)
    def websocket_disconnect(self, event):
        print("disconnected .....", event)
        raise StopConsumer()


class MyASyncConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        print("connected .....", event)
        await self.send({
            'type':'websocket.accept',
        })

    async def websocket_receive(self, event):
        print("receiving .....", event)
        print("message", event['text'])

        for i in range(50):
            await self.send({
                'type':'websocket.send',
                'text':str(i)
            })
            asyncio.sleep(1)
            print("hello")
    async def websocket_disconnect(self, event):
        print("disconnected .....", event)
        raise StopConsumer()