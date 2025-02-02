import vampytest

from ..fields import put_keywords_into


def test__put_keywords_into():
    """
    Tests whether ``put_keywords_into`` is working as intended.
    """
    for input_, defaults, expected_output in (
        (None, False, {}),
        (None, True, {'keyword_filter': []}),
        (('a', ), False, {'keyword_filter': ['a']}),
    ):
        data = put_keywords_into(input_, {}, defaults)
        vampytest.assert_eq(data, expected_output)
