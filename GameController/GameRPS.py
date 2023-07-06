from Figures.Paper import Paper
from Figures.Rock import Rock
from Figures.Scissors import Scissors
from GameController.Game import Game


class GameRPS(Game):
    def __init__(self):
        super().__init__([Rock(), Paper(), Scissors()])
