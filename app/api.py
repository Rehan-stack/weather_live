import requests




def get_weather(city):
    url = f'http://api.weatherapi.com/v1/current.json?key=0a1e865be5624864b3251455232009%20&q={city}'
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
        
    else:
        return None
    


