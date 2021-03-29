import requests
from bs4 import BeautifulSoup

URL = 'https://www.amazon.com.tr/Anker-PowerCore-20000mAh-Powerbank-PowerIQ/dp/B07XKFV145?ref_=Oct_DLandingS_D_ed1e01eb_60&smid=A1UNQM1SR2CHM'

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"}

def check_price():
    
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')
    # print(soup.prettify())
    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_dealprice").get_text()
    # converted_price = price[0:4]
    converted_price = float(price[1:4])

    # if(converted_price < 140):
    #     send_mail()


    print(title.strip())
    # print(price.strip())
    # print(converted_price.strip())
    print(converted_price)

