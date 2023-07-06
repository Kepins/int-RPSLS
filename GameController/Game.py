from Enums.GameResultEnum import GameResultEnum
from Figures.Figure import Figure
import random


class Game:
    def __init__(self, figures: list[Figure]):
        self.figures = figures

    def get_possible_choices(self) -> list[Figure]:
        return self.figures

    def set_user_choice(self, figure: Figure) -> None:
        self.user_choice = figure

    def set_opponent_choice(self) -> None:
        self.opponent_choice = random.choice(self.figures)

    def get_opponent_choice(self) -> Figure:
        return self.opponent_choice

    def get_result(self) -> GameResultEnum:
        return self.user_choice.beats(self.opponent_choice)
