import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
import student.routing
import chat.routing
import Practice.routing
from channels.auth import AuthMiddlewareStack
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chatApp.settings')

application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket':AuthMiddlewareStack( URLRouter(
        student.routing.websocket_urlpatterns +
        chat.routing.websocket_urlpatterns +
        Practice.routing.websocket_urlpatterns
    )
    )
})