import requests
from twilio.rest import Client
import keys

client = Client(keys.account_sid, keys.auth_token)

message = client.messages.create(
    body="This is a test message!",
    from_ = keys.twilio_number,
    to = keys.target_number 
)

print(message.body)

api_key = '04d30ff35dffb5923aa11546c2059bfc'

city = 'Taipei'

url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

response = requests.get(url)

print(api_key)

# call API and get information about the rain, weather, amount of rainfall

if response.status_code == 200:
    data = response.json()
    temp = data['main']['temp']
    desc = data['weather'][0]['description']
    print(f'Temperature: {temp} K')
    print(f'Description: {desc}')
else:
    print('Error fetching weather data')

# if there is rain or a certain amount of rainfall send an email or text to me somehow? 
# I think i would need another API for this