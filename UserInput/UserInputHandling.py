import functools
from enum import Enum

from UserInput.AnswerOption import AnswerOption


def get_decision(question: str, answers: list[AnswerOption]) -> Enum:
    # read input from user
    user_input = input(question)
    # all valid user inputs that can be inserted
    valid_decisions = functools.reduce(lambda res, a: res+a, [a.matching_inputs for a in answers])

    # loop until user inserts valid input
    while user_input not in valid_decisions:
        user_input = input("Not a valid option!" + question)

    # find which answer it matches and what should be returned
    for answer in answers:
        if user_input in answer.matching_inputs:
            return answer.return_value
