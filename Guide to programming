import urllib.request
def get_price():
    page = urllib.request.urlopen("http://www.williamlong.info")
    text = page.read().decode("utf8")
    where = text.find("ba")
    start_of_price = where + 2
    end_of_price = start_of_price + 2
    return (text[start_of_price:end_of_price])
print(get_price())
