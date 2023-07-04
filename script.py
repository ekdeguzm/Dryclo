import requests

api_key = '04d30ff35dffb5923aa11546c2059bfc'

city = 'Taipei'

url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

response = requests.get(url)

print(api_key)

if response.status_code == 200:
    data = response.json()
    temp = data['main']['temp']
    desc = data['weather'][0]['description']
    print(f'Temperature: {temp} K')
    print(f'Description: {desc}')
else:
    print('Error fetching weather data')