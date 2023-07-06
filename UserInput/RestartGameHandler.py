from Enums.GameRestartEnum import GameRestartEnum
from UserInput.AnswerOption import AnswerOption
from UserInput.UserInputHandler import UserInputHandler


class RestartGameHandler(UserInputHandler):
    def __init__(self):
        super().__init__("Do you want to play again?[y/n]: ",
                         [AnswerOption(['y', 'Y'], GameRestartEnum.PLAY),
                          AnswerOption(['n', 'N'], GameRestartEnum.END_PROGRAM)]
                         )
