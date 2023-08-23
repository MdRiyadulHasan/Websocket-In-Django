from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer, JsonWebsocketConsumer, AsyncJsonWebsocketConsumer
from time import sleep
import asyncio

class MyWebSocketConsumer(WebsocketConsumer):
    def connect(self):
        print("Connected ..")
        self.accept()

    def receive(self, text_data=None, bytes_data=None):
        print("Received data from client", text_data)
        for i in range(50):
            self.send(text_data = str(i))
            sleep(1)

    def disconnect(self, close_code):
       print("Disconnected ..", close_code)

class MyAsyncWebsocketConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        print("Connected ..")
        await self.accept()

    async def receive(self, text_data=None, bytes_data=None):
        print("Received data from client", text_data)
        for i in range(50):
            await self.send(text_data = str(i))
            await asyncio.sleep(1)
        
    async def disconnect(self, close_code):
       print("Disconnected ..", close_code)

class MyJsonWebsocketConsumer(JsonWebsocketConsumer):
    def connect(self):
        print("Connected .. json websocket consumer..")
        self.accept()
    def receive_json(self, content, **kwargs):
        print("receving data from client", content)
        print("type", type(content))

        for i in range(30):
            self.send_json({
                "message": str(i),
            })
            sleep(1)
    def disconnect(self, close_code):
        print("Disconnected .. json websocket consumer", close_code)

class MyAsyncJsonWebsocketConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        print("Connected .. json websocket consumer..")
        await self.accept()

    async def receive_json(self, content, **kwargs):
        print("receving data from client", content)
        for i in range(50):
            await self.send_json({
                "message": str(i),
            })
            await asyncio.sleep(1)

    async def disconnect(self, close_code):
        print("Disconnected .. json websocket consumer", close_code)