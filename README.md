# Dry Clothes Bot

<div align="center">
    <img alt="Screenshot" src="files/dry_clothes_bot_3.png" width="800px" height="600px">
</div>



## Intro

### Problem
I lived in Taiwan for a year to learn Chinese. Due to not having access to a drying machine, hanging my clothes outside a part of my routine. However, the region's humid climate and frequent rain showers occasionally left me with the unintended inconvenience of damp clothing.

### Solution
This program leverages the OpenWeatherMap API to retrieve weather information for Taipei and then sends a text message using the Twilio service to notify the user about the weather conditions, with a specific focus on rain. It extracts key weather details, including weather type, description, temperature, humidity, and wind speed. If rain is detected, it informs the user, advising actions like bringing in clothes if necessary. If no rain is indicated, it sends a message stating that it's not raining and provides general weather information. The program is designed to assist users in making weather-informed decisions for their day in Taipei.

## Table of Contents
- [Usage](#Usage)
- [License](#License)

## Usage
To automate the execution of the weather notification program and send text messages every day, I used the crontab job scheduler in a Bash script following these steps:

Use the crontab command to edit crontab file. Open crontab configuration by running:

```bash
crontab -e
```

To run Bash script daily, I added the following line to my crontab file. This example schedules the job to run at 8:00 AM every day. 

```bash
0 8 * * * /path/to/dry_clothes_bot/main.py
```
## License
My Dry Clothes Bot project is licensed under the MIT License Copyright (c) 2023.

See the [LICENSE](https://github.com/ekdeguzm/dry_clothes_bot/LICENSE) for information on the history of this software, terms & conditions for usage, and a DISCLAIMER OF ALL WARRANTIES.

All trademarks referenced herein are property of their respective holders.