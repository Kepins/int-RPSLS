from Enums.GameModeEnum import GameModeEnum
from UserInput.AnswerOption import AnswerOption
from UserInput.UserInputHandler import UserInputHandler


class ExtendedVersionHandler(UserInputHandler):
    def __init__(self):
        super().__init__("Do you want to play extended version?[y/n]: ",
                         [AnswerOption(['y', 'Y'], GameModeEnum.RPSLS),
                          AnswerOption(['n', 'N'], GameModeEnum.RPS)]
                         )
