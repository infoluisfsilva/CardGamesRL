class Trick:
    def __init__(self, leader):
        self.leader = leader
        self.plays = []  # list of (player, card)

    def add_play(self, player, card):
        self.plays.append((player, card))

    @property
    def lead_suit(self):
        if not self.plays:
            return None
        return self.plays[0][1].suit

    def is_complete(self, player_count):
        return len(self.plays) == player_count