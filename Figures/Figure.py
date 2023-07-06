from __future__ import annotations

from abc import abstractmethod, ABC

from Enums.FiguresEnum import FiguresEnum
from Enums.GameResultEnum import GameResultEnum


class Figure(ABC):
    def __init__(self, figure: FiguresEnum, wins_with: list[FiguresEnum]):
        self.figure = figure
        self.wins_with = wins_with

    @property
    @abstractmethod
    def name(self) -> str:
        pass

    def beats(self, other: Figure) -> GameResultEnum:
        if other.figure in self.wins_with:
            return GameResultEnum.WIN
        if self.figure == other.figure:
            return GameResultEnum.TIE
        return GameResultEnum.LOSS
