import random

class Deck:
    def __init__(self, cards):
        self._cards = list(cards)

    def shuffle(self):
        random.shuffle(self._cards)

    def draw(self):
        if not self._cards:
            raise ValueError("Deck is empty")
        return self._cards.pop()

    def deal(self, n):
        return [self.draw() for _ in range(n)]

    def __len__(self):
        return len(self._cards)