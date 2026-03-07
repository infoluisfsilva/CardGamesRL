from dataclasses import dataclass

@dataclass(frozen=True)
class Card:
    suit: str
    rank: str

    def __str__(self):
        return f"{self.rank} of {self.suit}"
    

from enum import Enum

class Suit(Enum):
    HEARTS = "hearts"
    SPADES = "spades"
    CLUBS = "clubs"
    DIAMONDS = "diamonds"