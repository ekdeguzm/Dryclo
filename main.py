import requests
from twilio.rest import Client
import keys

"""
Function to send a text message to the user explaining that it is raining
"""

client = Client(keys.account_sid, keys.auth_token)

api_key = '04d30ff35dffb5923aa11546c2059bfc'

city = 'Taipei'

url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

response = requests.get(url)

# def send_text():
#     # logic to send a text message

#     # I moved the logic that you had into this function definition, functions are
#     # a good way to organize pieces of functionality that you might want to reuse, and help your
#     # code to look cleaner, for more info see here https://en.wikipedia.org/wiki/Function_(computer_programming)

#     # if there is rain or a certain amount of rainfall send an email or text to me somehow?
#     # I think i would need another API for this

#     message = client.messages.create(
#         body="It is raining! Get your clothes today",
#         from_=keys.twilio_number,
#         to=keys.target_number
#     )

#     print(message.body)


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
    rain_mm = data['rain']['1h']
    # convert mm to inches
    rain_in = (rain_mm / 25.4)

    print(f'Weather Type: {main}')
    print(f'Description: {desc.title()}')
    print(f'Temperature: {round(temp_F)} F')
    print(f'Humidity: {humidity} %' )
    print(f'Wind: {wind_mph:.1f} mph')
    print(f'Last Hour\'s Rain: {rain_in} inches')

    # I added this try/except block to your code to catch any errors. Try/except or try/catch blocks are the
    # standard way to catch errors in programming. The logic that you want to execute is in the try block,
    # and the logic that you want to execute in case an exception is thrown is put into the except block

    # with the previous logic, if the words rain or Rain were not found then it was mentioned that there was
    # an error fetching the weather data. This is not necessarily true since the weather data could have
    # been retrieved correctly but just that it it sunny that day. I updated the else clause accordingly.

    try:
            if 'rain' in desc or 'Rain' in desc:
                print('Its raining!!! Get your clothes')

                # send text method call here
                send_text()
            else:
                print('It\'s not raining today, no worries')
    except:
        print('Error fetching weather data')