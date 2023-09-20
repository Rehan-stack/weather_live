import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .api import get_weather


class weather_consumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
    

    async def disconnect(self, code):
        return await super().disconnect(code)
    

    async def receive(self, text_data):
        new = {'city':text_data}
        str_data = json.dumps(new)
        data = json.loads(str_data)
        city = data['city']
     

        wether = get_weather(city)
        await self.send(text_data=json.dumps(wether))


