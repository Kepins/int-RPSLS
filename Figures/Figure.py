from __future__ import annotations

from abc import abstractmethod, ABC

from Enums.FiguresEnum import FiguresEnum
from Enums.GameResultEnum import GameResultEnum


class Figure(ABC):
    """
        Abstract class that represents one figure that user can choose.
    """
    def __init__(self, figure: FiguresEnum, wins_with: list[FiguresEnum]):
        self.figure = figure
        self.wins_with = wins_with

    @property
    @abstractmethod
    def name(self) -> str:
        """Human-readable name"""
        pass

    def beats(self, other: Figure) -> GameResultEnum:
        """Check if own figure beats other figure"""
        if other.figure in self.wins_with:
            return GameResultEnum.WIN
        if self.figure == other.figure:
            return GameResultEnum.TIE
        return GameResultEnum.LOSS
