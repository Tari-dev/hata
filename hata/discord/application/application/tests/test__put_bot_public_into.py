import vampytest

from ..fields import put_bot_public_into


def test__put_bot_public_into():
    """
    Tests whether ``put_bot_public_into`` works as intended.
    """
    for input_, defaults, expected_output in (
        (False, False, {}),
        (False, True, {'bot_public': False}),
        (True, False, {'bot_public': True}),
    ):
        data = put_bot_public_into(input_, {}, defaults)
        vampytest.assert_eq(data, expected_output)
