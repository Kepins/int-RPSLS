from Enums.GameResultEnum import GameResultEnum
from Figures.Lizard import Lizard
from Figures.Paper import Paper
from Figures.Rock import Rock
from Figures.Scissors import Scissors
from Figures.Spock import Spock


def test_name_paper():
    paper = Paper()
    assert paper.name == "Paper"


def test_ties_against_paper():
    paper = Paper()
    paper2 = Paper()
    assert paper.beats(paper2) == GameResultEnum.TIE


def test_wins_against_spock():
    paper = Paper()
    spock = Spock()
    assert paper.beats(spock) == GameResultEnum.WIN


def test_looses_against_scissors():
    paper = Paper()
    scissors = Scissors()
    assert paper.beats(scissors) == GameResultEnum.LOSS


def test_wins_against_rock():
    paper = Paper()
    rock = Rock()
    assert paper.beats(rock) == GameResultEnum.WIN


def test_looses_against_lizard():
    paper = Paper()
    lizard = Lizard()
    assert paper.beats(lizard) == GameResultEnum.LOSS
