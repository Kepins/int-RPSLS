from Enums.GameResultEnum import GameResultEnum
from Figures.Lizard import Lizard
from Figures.Paper import Paper
from Figures.Rock import Rock
from Figures.Scissors import Scissors
from Figures.Spock import Spock


def test_name_lizard():
    lizard = Lizard()
    assert lizard.name == "Lizard"


def test_wins_against_paper():
    lizard = Lizard()
    paper = Paper()
    assert lizard.beats(paper) == GameResultEnum.WIN


def test_wins_against_spock():
    lizard = Lizard()
    spock = Spock()
    assert lizard.beats(spock) == GameResultEnum.WIN


def test_looses_against_scissors():
    lizard = Lizard()
    scissors = Scissors()
    assert lizard.beats(scissors) == GameResultEnum.LOSS


def test_looses_against_rock():
    lizard = Lizard()
    rock = Rock()
    assert lizard.beats(rock) == GameResultEnum.LOSS


def test_ties_against_lizard():
    lizard = Lizard()
    lizard2 = Lizard()
    assert lizard.beats(lizard2) == GameResultEnum.TIE
