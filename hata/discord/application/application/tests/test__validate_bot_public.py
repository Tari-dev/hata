import vampytest

from ..fields import validate_bot_public


def test__validate_bot_public__0():
    """
    Tests whether `validate_bot_public` works as intended.
    
    Case: passing.
    """
    for input_value, expected_output in (
        (True, True),
        (False, False)
    ):
        output = validate_bot_public(input_value)
        vampytest.assert_eq(output, expected_output)


def test__validate_bot_public__1():
    """
    Tests whether `validate_bot_public` works as intended.
    
    Case: `TypeError`.
    """
    for input_value in (
        12.6,
    ):
        with vampytest.assert_raises(TypeError):
            validate_bot_public(input_value)
