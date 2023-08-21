from channels.consumer import SyncConsumer, AsyncConsumer
# from channels.generic.websocket import AsyncConsumer
from channels.exceptions import StopConsumer

class mySyncConsumer(SyncConsumer):
    def websocket_connect(self,event):
        print("Riyad conneted.......Riyad", event)
        self.send({
            'type': 'websocket.accept'
        })

    def websocket_receive(self,event):

        print("receiving message ...", event)
        print("Message is : ", event['text'])

        self.send({
            'type':'websocket.send',
            'text': 'Message sent to client'

        })

    def websocket_disconnect(self, event):
        print("disconnected", event)
        raise StopConsumer()

class myASyncConsumer(AsyncConsumer):
    async def websocket_connect(self,event):
        print(" Async conneted Riyad Vai ", event)
        await self.send({
            'type': 'websocket.accept'
        })
    async def websocket_receive(self,event):
        print(" Async receiving message ...",event)
        print("Message is : ", event['text'])

        await self.send({
            'type':'websocket.send',
            'text':'Message sent to client'
        })

    async def websocket_disconnect(self, event):
        print("Async disconnected",event)
        raise StopConsumer()