# Install pandas, requests, BeautifulSoup
import pandas as pd
import requests
from bs4 import BeautifulSoup


page = requests.get('https://forecast.weather.gov/MapClick.php?lat=44.9055&lon=-122.8107&lg=english&FcstType=text#.XqmLAp4zbIU')
soup = BeautifulSoup(page.content, 'html.parser')
week = soup.find(id='seven-day-forecast-body')
# print(week)
items = week.find_all(class_='tombstone-container')

print(items[0].find(class_='period-name').get_text())
print(items[0].find(class_='short-desc').get_text())
print(items[0].find(class_='temp').get_text())

period_name = [item.find(class_='period-name').get_text() for item in items]
short_description = [item.find(class_='short-desc').get_text() for item in items]
temperatures = [item.find(class_='temp').get_text() for item in items]


# print(period_name)
# print(short_description)
# print(temperatures)

weather_stuff = pd.DataFrame({
    'period': period_name,
    'short_description': short_description,
    'temperatures': temperatures
})

print(weather_stuff)

weather_stuff.to_csv('weather.pdf')