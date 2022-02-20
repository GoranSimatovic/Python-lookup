from bs4 import BeautifulSoup
import requests
import re

URL = 'https://www.meteo-info.hr/index1.php?app=grad/zagreb'
page = requests.get(URL)

meteo_info = BeautifulSoup(page.content, 'html.parser')
results = meteo_info.find(id='danasnja')

result = re.search('<li class="temperatura">(.*)°C</li>', str(results.find_all('li', class_='temperatura')))
temperatura = float(result.group(1))
print(temperatura)