import functools
from typing import Any

from UserInteraction.AnswerOption import AnswerOption


class UserInputHandler:
    def __init__(self, question: str, answers: list[AnswerOption]):
        self.question = question
        self.answers = answers

    def get_decision(self) -> Any:
        # read input from user
        user_input = input(self.question)
        # all valid user inputs that can be inserted
        valid_decisions = functools.reduce(lambda res, a: res + a,
                                           [a.matching_inputs for a in self.answers])

        # loop until user inserts valid input
        while user_input not in valid_decisions:
            user_input = input("Not a valid option! " + self.question)

        # find which answer it matches and what should be returned
        for answer in self.answers:
            if user_input in answer.matching_inputs:
                return answer.return_value
        # should never be reached
        return None
