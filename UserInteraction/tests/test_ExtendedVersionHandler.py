import builtins
from unittest import mock

from Enums.GameModeEnum import GameModeEnum
from UserInteraction.ExtendedVersionHandler import ExtendedVersionHandler


def test_wants_extended_version():
    handler = ExtendedVersionHandler()

    with mock.patch.object(builtins, 'input', lambda _: 'y'):
        assert handler.get_decision() == GameModeEnum.RPSLS


def test_wants_extended_version2():
    handler = ExtendedVersionHandler()

    with mock.patch.object(builtins, 'input', lambda _: 'Y'):
        assert handler.get_decision() == GameModeEnum.RPSLS


def test_doesnt_want_extended_version():
    handler = ExtendedVersionHandler()

    with mock.patch.object(builtins, 'input', lambda _: 'n'):
        assert handler.get_decision() == GameModeEnum.RPS


def test_doesnt_want_extended_version2():
    handler = ExtendedVersionHandler()

    with mock.patch.object(builtins, 'input', lambda _: 'N'):
        assert handler.get_decision() == GameModeEnum.RPS


def test_wrong_input_than_want():
    handler = ExtendedVersionHandler()

    input_iter = iter(['bad input', 'y'])

    with mock.patch.object(builtins, 'input', lambda _: next(input_iter)):
        assert handler.get_decision() == GameModeEnum.RPSLS


def test_wrong_input_than_dont_want():
    handler = ExtendedVersionHandler()

    input_iter = iter(['bad input', 'nasdaq', 'N'])

    with mock.patch.object(builtins, 'input', lambda _: next(input_iter)):
        assert handler.get_decision() == GameModeEnum.RPS
