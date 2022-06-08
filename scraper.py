import re


def get_whisky_name(row):
    # scraping a name of the whisky
    return row.find(
        "a",
        attrs={"mp-whisky-item-name"}).get_text().strip()


def get_whisky_url(row):
    # scraping url of the whisky
    return row.find(
        "a",
        attrs={"mp-whisky-item-name"})['href']


def get_bottle_img_url(row):
    # scraping url of a whisky image
    return row.find(
        "img",
        attrs={"unveil"})['data-src']


def get_bottle_price(row):
    # scraping a price
    price = row.find(
        "div",
        attrs={"mp-whisky-item-price"}).get_text().strip()

    if price[0] == '€':
        return price
    else:
        return row.find(
            "div",
            attrs={"mp-whisky-item-price-converted"}).get_text().strip()


def get_whisky_rating(row):
    # scraping the whisky rating
    temp = row.find(
        "dl",
        attrs={"dl-horizontal"}).get_text().strip()

    pattern_rating = re.compile(r'[^\s]+')
    rating = pattern_rating.search(temp)

    return rating.group()


def get_user_rating(row):
    # scraping user rating
    user_rating = str(row.find(
        "div",
        attrs={"bottle-rating"}))

    return user_rating


def get_amount_of_ratings(row):
    # scraping user ratings
    return row.find(
        "span",
        attrs={"bottle-rating-votes"}).get_text().strip()
