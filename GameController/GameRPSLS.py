from Figures.Lizard import Lizard
from Figures.Paper import Paper
from Figures.Rock import Rock
from Figures.Scissors import Scissors
from Figures.Spock import Spock
from GameController.Game import Game


class GameRPSLS(Game):
    def __init__(self):
        super().__init__([Rock(), Paper(), Scissors(), Lizard(), Spock()])
