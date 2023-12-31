from Enums.FiguresEnum import FiguresEnum
from Figures.Figure import Figure


class Rock(Figure):
    """Rock figure"""
    name = "Rock"

    def __init__(self):
        super().__init__(FiguresEnum.ROCK, [FiguresEnum.SCISSORS, FiguresEnum.LIZARD])
