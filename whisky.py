class Whisky:
    whisky_name: str
    whisky_url: str
    bottle_image_url: str
    whisky_rating: float
    user_rating: float
    amount_of_ratings: int
    bottle_price: float

    def __init__(self,
                 whisky_name: str,
                 whisky_url: str,
                 bottle_image_url: str,
                 whisky_rating: float,
                 user_rating: float,
                 amount_of_ratings: int,
                 bottle_price: float):
        self.whisky_name = whisky_name
        self.whisky_url = whisky_url
        self.bottle_image_url = bottle_image_url
        self.whisky_rating = whisky_rating
        self.user_rating = user_rating
        self.amount_of_ratings = amount_of_ratings
        self.bottle_price = bottle_price

    def __str__(self):
        return {
            "Whisky name": self.whisky_name,
            "Whisky URL address": self.whisky_url,
            "Bottle URL address": self.bottle_image_url,
            "Whisky rating": self.whisky_rating,
            "User rating": self.user_rating,
            "Amount of user ratings": self.amount_of_ratings,
            "Bottle price": self.bottle_price
        }
