import requests
from bs4 import BeautifulSoup

page = requests.get("https://forecast.weather.gov/MapClick.php?lat=42.3317&lon=-83.048#.X3dAMy9h2gA")
soup = BeautifulSoup(page.content, 'html.parser')
forecast = soup.find(id= "seven-day-forecast")
f_items = forecast.find_all(class_= "tombstone-container")
seven_day = [print(i.find(class_='period-name').get_text() +'\n'+ 
            i.find(class_='short-desc').get_text()+'\n'+ 
            i.find(class_='temp').get_text() + '\n') 
            for i in f_items]

