from Enums.FiguresEnum import FiguresEnum
from Figures.Figure import Figure


class Paper(Figure):
    def __init__(self):
        super().__init__(FiguresEnum.PAPER, [FiguresEnum.ROCK, FiguresEnum.SPOCK])
