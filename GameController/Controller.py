from Enums.GameModeEnum import GameModeEnum
from Enums.GameRestartEnum import GameRestartEnum
from GameController.GameRPS import GameRPS
from GameController.GameRPSLS import GameRPSLS
from UserInput.ExtendedVersionHandler import ExtendedVersionHandler
from UserInput.RestartGameHandler import RestartGameHandler


class Controller:
    extendedVersionHandler = ExtendedVersionHandler()
    restartGameHandler = RestartGameHandler()

    def start(self) -> None:

        # player wants to play until is_playing is set to GameRestart.END_PROGRAM
        is_playing = GameRestartEnum.PLAY
        while is_playing != GameRestartEnum.END_PROGRAM:
            game_mode: GameModeEnum = self.extendedVersionHandler.get_decision()

            game = None
            if game_mode == GameModeEnum.RPS:
                game = GameRPS()
            elif game_mode == GameModeEnum.RPSLS:
                game = GameRPSLS()


            is_playing = self.restartGameHandler.get_decision()
