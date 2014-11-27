import urllib.request
import time
def get_price():
    page = urllib.request.urlopen("http://www.williamlong.info")
    text = page.read().decode("utf8")
    where = text.find("ba")
    start_of_price = where + 2
    end_of_price = start_of_price + 2
    return (text[start_of_price:end_of_price])
price_now = input("Do you want to see the price now (Y/N)\n")
if price_now == "Y":
    print(get_price())
else:
    price = 99
    while price > 4:
        time.sleep(900)
        price =get_price()
    print("BUY!")
