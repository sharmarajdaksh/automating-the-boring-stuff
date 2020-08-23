import bs4
import requests

amazon_kindle_url = 'https://www.amazon.in/All-New-Kindle-Paperwhite-10th-Built/dp/B077454Z99/ref=sr_1_3'
headers = { "User-Agent" : "Defined" }
res = requests.get(amazon_kindle_url, headers = headers)
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, 'html.parser')

price_html_elements = soup.select('#price_inside_buybox')

amazon_kindle_price = price_html_elements[0].text.strip()

print(amazon_kindle_price)
