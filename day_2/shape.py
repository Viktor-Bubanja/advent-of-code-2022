from constants import *


class Shape:
    def __init__(self, rock=False, paper=False, scissors=False):
        self.rock = rock
        self.paper = paper
        self.scissors = scissors
        assert rock + paper + scissors == 1

        self.score = self.rock * ROCK_SCORE + self.paper * PAPER_SCORE + self.scissors * SCISSORS_SCORE

    @classmethod
    def build(cls, encrypted_shape):
        assert encrypted_shape in VALID_SHAPES
        if encrypted_shape == PLAYER_ROCK or encrypted_shape == OPPONENT_ROCK:
            return cls(rock=True)
        elif encrypted_shape == PLAYER_PAPER or encrypted_shape == OPPONENT_PAPER:
            return cls(paper=True)
        elif encrypted_shape == PLAYER_SCISSORS or encrypted_shape == OPPONENT_SCISSORS:
            return cls(scissors=True)

    def __eq__(self, other):
        return (
            self.rock and other.rock
        ) or (
            self.paper and other.paper
        ) or (
            self.scissors and other.scissors
        )

    def __gt__(self, other):
        return (
            self.rock and other.scissors
        ) or (
            self.paper and other.rock
        ) or (
            self.scissors and other.paper
        )

    def __lt__(self, other):
        return not self > other and not self == other
