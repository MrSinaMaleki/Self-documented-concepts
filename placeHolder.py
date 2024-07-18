class Bag:
    def __init__(self):
        self.storage = []


class Player:
    def __init__(self, name):
        self.name = name
        self.bag = Bag()  # Composite


class Game:
    def __init__(self, player_name1, player_name2):
        self.players = [
            Player(player_name1),
            Player(player_name2)
        ]


my_g = Game("Fatemeh", "Ali")
