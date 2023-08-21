import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
import student.routing
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chatApp.settings')

application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': URLRouter(
        student.routing.websocket_urlpatterns
    )
})