from Enums.GameResultEnum import GameResultEnum
from Figures.Lizard import Lizard
from Figures.Paper import Paper
from Figures.Rock import Rock
from Figures.Scissors import Scissors
from Figures.Spock import Spock


def test_name_spock():
    spock = Spock()
    assert spock.name == "Spock"


def test_looses_against_paper():
    spock = Spock()
    paper = Paper()
    assert spock.beats(paper) == GameResultEnum.LOSS


def test_ties_against_spock():
    spock = Spock()
    spock2 = Spock()
    assert spock.beats(spock2) == GameResultEnum.TIE


def test_wins_against_scissors():
    spock = Spock()
    scissors = Scissors()
    assert spock.beats(scissors) == GameResultEnum.WIN


def test_wins_against_rock():
    spock = Spock()
    rock2 = Rock()
    assert spock.beats(rock2) == GameResultEnum.WIN


def test_looses_against_lizard():
    spock = Spock()
    lizard = Lizard()
    assert spock.beats(lizard) == GameResultEnum.LOSS