from Enums.GameResultEnum import GameResultEnum
from Figures.Lizard import Lizard
from Figures.Paper import Paper
from Figures.Rock import Rock
from Figures.Scissors import Scissors
from Figures.Spock import Spock


def test_name_scissors():
    scissors = Scissors()
    assert scissors.name == "Scissors"


def test_wins_against_paper():
    scissors = Scissors()
    paper = Paper()
    assert scissors.beats(paper) == GameResultEnum.WIN


def test_looses_against_spock():
    scissors = Scissors()
    spock = Spock()
    assert scissors.beats(spock) == GameResultEnum.LOSS


def test_ties_against_scissors():
    scissors = Scissors()
    scissors = Scissors()
    assert scissors.beats(scissors) == GameResultEnum.TIE


def test_looses_against_rock():
    scissors = Scissors()
    rock2 = Rock()
    assert scissors.beats(rock2) == GameResultEnum.LOSS


def test_wins_against_lizard():
    scissors = Scissors()
    lizard = Lizard()
    assert scissors.beats(lizard) == GameResultEnum.WIN
