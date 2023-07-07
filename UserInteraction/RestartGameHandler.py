from Enums.GameRestartEnum import GameRestartEnum
from UserInteraction.AnswerOption import AnswerOption
from UserInteraction.UserInputHandler import UserInputHandler


class RestartGameHandler(UserInputHandler):
    """
        Questions user about restarting game
    """

    def __init__(self):
        super().__init__("Do you want to play again?[y/n]: ",
                         [AnswerOption(['y', 'Y'], GameRestartEnum.PLAY),
                          AnswerOption(['n', 'N'], GameRestartEnum.END_PROGRAM)]
                         )
