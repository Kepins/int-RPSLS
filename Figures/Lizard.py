from Enums.FiguresEnum import FiguresEnum
from Figures.Figure import Figure


class Lizard(Figure):
    def __init__(self):
        super().__init__(FiguresEnum.LIZARD, [FiguresEnum.PAPER, FiguresEnum.SPOCK])
