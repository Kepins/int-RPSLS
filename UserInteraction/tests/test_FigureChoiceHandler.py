import builtins
from unittest import mock

from Figures.Lizard import Lizard
from Figures.Paper import Paper
from Figures.Rock import Rock
from Figures.Scissors import Scissors
from Figures.Spock import Spock
from UserInteraction.FigureChoiceHandler import FigureChoiceHandler


def test_wants_first_figure():
    # figures used in test case
    figures = [Rock(), Paper(), Scissors()]

    handler = FigureChoiceHandler(figures)

    with mock.patch.object(builtins, 'input', lambda _: '1'):
        assert handler.get_decision() == figures[0]


def test_wants_last_figure():
    # figures used in test case
    figures = [Rock(), Paper(), Scissors(), Lizard(), Spock()]

    handler = FigureChoiceHandler(figures)

    with mock.patch.object(builtins, 'input', lambda _: f'{len(figures)}'):
        assert handler.get_decision() == figures[-1]


def test_bad_input_then_wants_last_figure():
    # figures used in test case
    figures = [Rock(), Paper(), Scissors(), Lizard(), Spock()]

    handler = FigureChoiceHandler(figures)

    input_iter = iter(['bad input', f'{len(figures)}'])

    with mock.patch.object(builtins, 'input', lambda _: next(input_iter)):
        assert handler.get_decision() == figures[-1]
