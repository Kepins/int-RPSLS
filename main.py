
from UserInput.UserInputHandling import get_decision
from UserInput.AnswerOption import AnswerOption

if __name__ == '__main__':

    extended_version = get_decision("Do you want to play extended version?[y/n]: ",
                                    [AnswerOption(['y', 'Y'], True),
                                     AnswerOption(['n', 'N'], False)])

    print(extended_version)
