from Figures.Figure import Figure
from UserInput.AnswerOption import AnswerOption
from UserInput.UserInputHandler import UserInputHandler


class FigureChoiceHandler(UserInputHandler):
    def __init__(self, figures: list[Figure]):
        question = "What figure do you want to choose?\n"
        answers = []
        for i, figure in enumerate(figures):
            question += f"{i+1}. {figure.name}\n"
            answers.append(AnswerOption([str(i+1)], figure))
        super().__init__(question, answers)
