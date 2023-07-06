from Enums.FiguresEnum import FiguresEnum
from Enums.GameModeEnum import GameModeEnum
from Enums.GameRestartEnum import GameRestartEnum
from Figures.Lizard import Lizard
from Figures.Paper import Paper
from Figures.Rock import Rock
from Figures.Scissors import Scissors
from Figures.Spock import Spock
from GameController.Game import Game
from UserInput.AnswerOption import AnswerOption
from UserInput.UserInputHandling import get_decision


class Controller:
    def start(self):

        # player wants to play until is_playing is set to GameRestart.END_PROGRAM
        is_playing = GameRestartEnum.PLAY
        while is_playing != GameRestartEnum.END_PROGRAM:
            game_mode = get_decision("Do you want to play extended version?[y/n]: ",
                                     [AnswerOption(['y', 'Y'], GameModeEnum.RPSLS),
                                      AnswerOption(['n', 'N'], GameModeEnum.RPS)])

            game = None
            if game_mode == GameModeEnum.RPS:
                game = Game([Rock(), Paper(), Scissors()])
            elif game_mode == GameModeEnum.RPSLS:
                game = Game([Rock(), Paper(), Scissors(), Lizard(), Spock()])

            is_playing = get_decision("Do you want to play again?[y/n]: ",
                                      [AnswerOption(['y', 'Y'], GameRestartEnum.PLAY),
                                       AnswerOption(['n', 'N'], GameRestartEnum.END_PROGRAM)])