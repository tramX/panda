from django.urls import re_path

from . import consumers


websocket_urlpatterns = [
    # re_path(r'ws/lesson/(?P<room_name>\w+)/$', consumers.WebRTCConsumer),
    re_path(r'ws/lesson/peerjs/$', consumers.WebRTCConsumer),
]