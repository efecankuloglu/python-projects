import requests
from bs4 import BeautifulSoup


URL = "https://www.amazon.com.tr/Yeni-Apple-iPhone-Pro-128-GB/dp/B09G9PCZGF/ref=cs_sr_dp_2?__mk_tr_TR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=1H94HLIU5KT9R&keywords=iphone%2B13%2Bpro&qid=1652375644&s=electronics&sprefix=iphone%2B13%2Bpro%2Celectronics%2C148&sr=1-4&th=1"

headers = {
    "Accept-Language": "tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36"
}

TELEGRAM_TOKEN = "5319529898:AAFkhZDtutK2tbTuCRL7AFP-gqTIEhq-p0c"
TELEGRAM_USERID = "1026625311"

response = requests.get(URL, headers=headers)

soup = BeautifulSoup(response.text, "html.parser")

product = soup.find("span", class_="a-size-large product-title-word-break").getText().strip()

price = soup.find("span", class_="a-price-whole").getText() + soup.find("span", class_="a-price-fraction").getText()

price = float(price.replace(".", "").replace(",", "."))

target_price = 20000.00

if price <= target_price:
    message = f"{product} is now {target_price}₺.\n{URL}"
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    data = {'chat_id': TELEGRAM_USERID, 'text': message}
    requests.post(url, data)
