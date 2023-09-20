from django.urls import path
from . import consumers

websocketurl_patterns = [
    path('ws/weather/<str:city>/',consumers.weather_consumer.as_asgi()),

]