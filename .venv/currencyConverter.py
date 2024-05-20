from bs4 import BeautifulSoup
import requests

def getCurrency(in_currency, out_currency):
    url = f"https://www.x-rates.com/calculator/?from={in_currency}&to={out_currency}&amount=1"
    content = requests.get(url).text
    soup = BeautifulSoup(content, 'html.parser')
    rate = soup.find("span", class_="ccOutputRslt").getText()
    rate = float(rate[0:-4])
    return rate



print(getCurrency("EUR", "AUD"))