from Enums.FiguresRPSLS import FiguresRPSLS
from Enums.FiguresRPS import FiguresRPS
from Enums.GameMode import GameMode
from Enums.GameRestart import GameRestart
from GameController.Game import Game
from UserInput.AnswerOption import AnswerOption
from UserInput.UserInputHandling import get_decision


class Controller:
    def start(self):

        # player wants to play until is_playing is set to GameRestart.END_PROGRAM
        is_playing = GameRestart.PLAY
        while is_playing != GameRestart.END_PROGRAM:
            game_mode = get_decision("Do you want to play extended version?[y/n]: ",
                                     [AnswerOption(['y', 'Y'], GameMode.RPSLS),
                                      AnswerOption(['n', 'N'], GameMode.RPS)])

            game = None
            if game_mode == GameMode.RPS:
                game = Game(list(FiguresRPS), [])
            elif game_mode == GameMode.RPSLS:
                game = Game(list(FiguresRPSLS), [])

            is_playing = get_decision("Do you want to play again?[y/n]: ",
                                      [AnswerOption(['y', 'Y'], GameRestart.PLAY),
                                       AnswerOption(['n', 'N'], GameRestart.END_PROGRAM)])
