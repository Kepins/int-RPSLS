from Enums.FiguresRPSLSEnum import FiguresRPSLSEnum
from Enums.FiguresRPSEnum import FiguresRPSEnum
from Enums.GameModeEnum import GameModeEnum
from Enums.GameRestartEnum import GameRestartEnum
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
                game = Game(list(FiguresRPSEnum), [])
            elif game_mode == GameModeEnum.RPSLS:
                game = Game(list(FiguresRPSLSEnum), [])

            is_playing = get_decision("Do you want to play again?[y/n]: ",
                                      [AnswerOption(['y', 'Y'], GameRestartEnum.PLAY),
                                       AnswerOption(['n', 'N'], GameRestartEnum.END_PROGRAM)])
