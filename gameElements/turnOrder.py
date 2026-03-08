class TurnOrder:

    def __init__(self, players):
        self.players = players
        self.index = 0

    def current(self):
        return self.players[self.index]

    def advance(self):
        self.index = (self.index + 1) % len(self.players)

    def set_current(self, player):
        self.index = self.players.index(player)

    def reverse(self):
        pass

    def remove(self, player):
        pass