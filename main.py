import requests
from twilio.rest import Client
import keys

"""
Function to send a text message to the user explaining that it is raining
"""

# set up twilio client
client = Client(keys.account_sid, keys.auth_token)

# define API parameters
api_key = '04d30ff35dffb5923aa11546c2059bfc'
city = 'Taipei'
url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

# fetch weather data
response = requests.get(url)

# create function to send text
def send_text(text):
    message = client.messages.create(
        body= '-' + text,
        from_= keys.twilio_number,
        to= keys.target_number
    )

    print(message.body)


# call API and get information about the rain, weather, amount of rainfall
if response.status_code == 200:
    data = response.json()
    print(data)
    # important information to convey: weather type, weather description, humidity, rain description. 
    main = data['weather'][0]['main']
    desc = data['weather'][0]['description']
    temp_K = data['main']['temp']
    temp_F = (9/5) * (temp_K - 273) + 32 
    humidity = data['main']['humidity']
    wind_mps = data['wind']['speed']
    # convert meters/second to miles/hour
    wind_mph = wind_mps * (2.23694)

    # I added this try/except block to your code to catch any errors. Try/except or try/catch blocks are the
    # standard way to catch errors in programming. The logic that you want to execute is in the try block,
    # and the logic that you want to execute in case an exception is thrown is put into the except block

    # with the previous logic, if the words rain or Rain were not found then it was mentioned that there was
    # an error fetching the weather data. This is not necessarily true since the weather data could have
    # been retrieved correctly but just that it it sunny that day. I updated the else clause accordingly.
    try:
            if 'rain' in desc or 'Rain' in desc:
                rain_mm = data['rain']['1h']
                # convert mm to inches
                rain_in = (rain_mm / 25.4)
                text_content = f'''
\n\n
It is going to rain today!
\n\n
If you are hanging clothes outside, please take them inside.
\n\n
If not, you can disregard this message.
\n     
Weather Type: {main}
Description: {desc.title()}
Temperature: {round(temp_F)} F
Humidity: {humidity} %
Wind: {wind_mph:.1f} mph
Past Hour's Rain: {rain_in:.1f} inches
                '''
                # send text method call here
                send_text(text_content)
            else:
                text_content = f'''
\n\n
It\'s not raining today, you can leave your clothes outside.
\n\n            
Weather Type: {main}
Description: {desc.title()}
Temperature: {round(temp_F)} F
Humidity: {humidity} %
Wind: {wind_mph:.1f} mph
                '''
                send_text(text_content)
    except:
        print('Error fetching weather data')