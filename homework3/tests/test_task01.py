from unittest.mock import Mock

from homework3.task01 import cache


def test_for_mistakes():
    """Test is it working or there are some mistakes before counting"""

    @cache(times=1)
    def function(args):
        return args

    assert function('try') == 'try'


def test_times_parameter():
    mock_func = Mock()
    mock_func.return_value = 'try'

    @cache(times=2)
    def function(args):
        return mock_func(args)

    _ = function(None)
    _ = function(None)
    _ = function(None)

    assert mock_func.call_count == 2