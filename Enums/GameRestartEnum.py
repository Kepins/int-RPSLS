from enum import Enum


class GameRestartEnum(Enum):
    """Decision about wanting to play the game"""
    PLAY = 1
    END_PROGRAM = 2
