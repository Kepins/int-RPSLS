from Enums.FiguresEnum import FiguresEnum
from Figures.Figure import Figure


class Spock(Figure):
    """Spock figure"""
    name = "Spock"

    def __init__(self):
        super().__init__(FiguresEnum.SPOCK, [FiguresEnum.SCISSORS, FiguresEnum.ROCK])
