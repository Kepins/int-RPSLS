import random
from Enums.GameResultEnum import GameResultEnum
from Figures.Figure import Figure


class Game:
    """
        Game where you set players' choices and check result
    """

    def __init__(self, figures: list[Figure]):
        self.figures = figures
        self.user_choice = None
        self.opponent_choice = None

    def get_possible_choices(self) -> list[Figure]:
        """Returns all choices that player/opponent can make"""
        return self.figures

    def set_user_choice(self, figure: Figure) -> None:
        """Set what user choose"""
        self.user_choice = figure

    def set_opponent_choice(self) -> None:
        """Get random figure for the opponent"""
        self.opponent_choice = random.choice(self.figures)

    def get_result(self) -> GameResultEnum:
        """Check result after setting choices"""
        return self.user_choice.beats(self.opponent_choice)
