from __future__ import annotations

from Enums.FiguresEnum import FiguresEnum


class Figure:
    def __init__(self, figure: FiguresEnum, wins_with: list[FiguresEnum]):
        self.figure = figure
        self.wins_with = wins_with

    def beats(self, other: Figure):
        if other.figure in self.wins_with:
            return True
        return False
