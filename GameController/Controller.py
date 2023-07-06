from Enums.GameModeEnum import GameModeEnum
from Enums.GameRestartEnum import GameRestartEnum
from GameController.GameRPS import GameRPS
from GameController.GameRPSLS import GameRPSLS
from UserInput.ExtendedVersionHandler import ExtendedVersionHandler
from UserInput.FigureChoiceHandler import FigureChoiceHandler
from UserInput.RestartGameHandler import RestartGameHandler


class Controller:
    extended_version_handler = ExtendedVersionHandler()
    restart_game_handler = RestartGameHandler()

    def start(self) -> None:

        # player wants to play until is_playing is set to GameRestart.END_PROGRAM
        is_playing = GameRestartEnum.PLAY
        while is_playing != GameRestartEnum.END_PROGRAM:
            game_mode: GameModeEnum = self.extended_version_handler.get_decision()

            game = None
            if game_mode == GameModeEnum.RPS:
                game = GameRPS()
            elif game_mode == GameModeEnum.RPSLS:
                game = GameRPSLS()

            figure_choice_handler = FigureChoiceHandler(game.get_possible_choices())

            game.set_user_choice(figure_choice_handler.get_decision())
            game.set_opponent_choice()
            print(game.get_opponent_choice())
            print(game.get_result())

            is_playing = self.restart_game_handler.get_decision()
