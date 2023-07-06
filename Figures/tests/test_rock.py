from Enums.GameResultEnum import GameResultEnum
from Figures.Lizard import Lizard
from Figures.Paper import Paper
from Figures.Rock import Rock
from Figures.Scissors import Scissors
from Figures.Spock import Spock


def test_name_rock():
    rock = Rock()
    assert rock.name == "Rock"


def test_looses_against_paper():
    rock = Rock()
    paper = Paper()
    assert rock.beats(paper) == GameResultEnum.LOSS


def test_looses_against_spock():
    rock = Rock()
    spock = Spock()
    assert rock.beats(spock) == GameResultEnum.LOSS


def test_wins_against_scissors():
    rock = Rock()
    scissors = Scissors()
    assert rock.beats(scissors) == GameResultEnum.WIN


def test_ties_against_rock():
    rock = Rock()
    rock2 = Rock()
    assert rock.beats(rock2) == GameResultEnum.TIE


def test_wins_against_lizard():
    rock = Rock()
    lizard = Lizard()
    assert rock.beats(lizard) == GameResultEnum.WIN
