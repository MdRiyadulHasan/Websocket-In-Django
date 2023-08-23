from django.urls import path
from . import consumers
websocket_urlpatterns =[
    path('ws/mim1/', consumers.MyWebSocketConsumer.as_asgi()),
    path('ws/mim2/', consumers.MyAsyncWebsocketConsumer.as_asgi()),
    path('ws/mim3/', consumers.MyJsonWebsocketConsumer.as_asgi()),
    path('ws/mim4/', consumers.MyAsyncJsonWebsocketConsumer.as_asgi()),
    # path('ws/mim2/<str:groupname>/', consumers.MyASyncConsumer.as_asgi()),
]