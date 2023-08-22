from django.urls import path
from . import consumers
websocket_urlpatterns =[
    path('ws/riyad1/', consumers.MySyncConsumer.as_asgi()),
    path('ws/riyad2/<str:groupname>/', consumers.MyASyncConsumer.as_asgi()),
]