import vampytest

from ..fields import validate_flags
from ..flags import ApplicationFlag


def iter_options__passing():
    yield 1, ApplicationFlag(1)
    yield ApplicationFlag(1), ApplicationFlag(1)


@vampytest._(vampytest.call_from(iter_options__passing()).returning_last())
def test__validate_flags__passing(input_value):
    """
    Tests whether `validate_flags` works as intended.
    
    Case: passing.
    
    Parameters
    ----------
    input_value : `object`
        The object to validate.
    
    Returns
    -------
    value : ``ApplicationFlag``
        The validated value.
    """
    output = validate_flags(input_value)
    vampytest.assert_instance(output, ApplicationFlag)
    return output


@vampytest.raising(TypeError)
@vampytest.call_with('a')
def test__validate_flags__type_error(input_value):
    """
    Tests whether `validate_flags` works as intended.
    
    Case: type error.
    
    Parameters
    ----------
    input_value : `object`
        The object to validate.
    
    Raises
    ------
    TypeError
        The raises exception.
    """
    validate_flags(input_value)
