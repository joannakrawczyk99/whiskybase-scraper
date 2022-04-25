import requests
from bs4 import BeautifulSoup
from scraper import get_whisky_name, get_whisky_url, get_bottle_img_url, get_whisky_rating, get_user_rating, \
    get_amount_of_ratings, get_bottle_price
from whisky import Whisky

URL_address = "https://www.whiskybase.com/market/browse?style=table&search=null&selling_method=&price=&shipsto" \
              "=&brand_id=&fillinglevel_id=&vintage_year=&bottler_id=&bottle_date_year= "

page_request = requests.get(URL_address, headers={
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 '
                  'Safari/537.36'})

bs = BeautifulSoup(page_request.content, "html.parser")

table = bs.find(
    "table",
    attrs={"class": "whiskytable"})

row_1 = table.tbody.find_all(
    "tr",
    attrs={"class": "mp-whisky-item-firstrow"})

row_2 = table.tbody.find_all(
    "tr",
    attrs={"class": "mp-whisky-item-secondrow"})

whisky_data = []

if len(row_1) == len(row_2):
    for i in range(len(row_1)):
        whisky_data.append(Whisky(
            get_whisky_name(row_1[i]),
            get_whisky_url(row_1[i]),
            get_bottle_img_url(row_1[i]),
            get_whisky_rating(row_2[i]),
            get_user_rating(row_2[i]),
            get_amount_of_ratings(row_2[i]),
            get_bottle_price(row_2[i])))

for i in whisky_data:
    print(i.__str__())
