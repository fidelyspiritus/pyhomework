import pytest

from homework3.task04 import (is_armstrong)


def test_is_armstrong():
    assert is_armstrong(153) is True, 'Is Armstrong number'
    assert is_armstrong(10) is False, 'Is not Armstrong number'
