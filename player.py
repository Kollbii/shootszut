class Player:
    # Checkout 0 - master out, 1 - single out, 2 - double out
    def __init__(self, name, points=501, checkout=2):
        self.name = name
        self.points = points
        self.checkout = checkout
        self.history = {
            self.points: 0
        }
        self.stats = {
            "60+": 0,
            "100+": 0,
            "120+": 0,
            "140+": 0,
            "160+": 0,
            "180": 0,
            "fl": 100, # put max int or smth later # fastest leg
            "hco": 0, # Highest checkout
        }

    def __str__(self):
        return "*"*24 + "\n" + str(self.name) + " has " + str(self.points) + " left"
    