from Enums.FiguresEnum import FiguresEnum
from Figures.Figure import Figure


class Scissors(Figure):
    def __init__(self):
        super().__init__(FiguresEnum.SCISSORS, [FiguresEnum.PAPER, FiguresEnum.LIZARD])
