from django.urls import path
from . import consumers
websocket_urlpatterns =[
    path('ws/mim1/', consumers.MySyncConsumer.as_asgi()),
    path('ws/mim2/<str:groupname>/', consumers.MyASyncConsumer.as_asgi()),
]