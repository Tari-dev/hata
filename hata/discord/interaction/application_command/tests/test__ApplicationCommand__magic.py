import vampytest

from ....localizations import Locale
from ....permission import Permission

from .. import ApplicationCommand, ApplicationCommandOption, ApplicationCommandOptionType, ApplicationCommandTargetType


def test__ApplicationCommand__len__0():
    """
    Tests whether ``ApplicationCommand.__len__`` works as intended if the minimal amount of fields are given at
    creation.
    
    We directly set `target_type`, so `description` can default to `None` instead of `str`
    """
    application_command = ApplicationCommand(
        'owo',
        None,
        target_type = ApplicationCommandTargetType.user,
    )
    
    return len(application_command)


def test__ApplicationCommand__len__1():
    """
    Tests whether ``ApplicationCommand.__len__`` works as intended if the maximal amount of fields are given at
    creation.
    """
    application_command = ApplicationCommand(
        'owo',
        'description',
        allow_in_dm = True,
        description_localizations = {
            Locale.thai: 'ayy',
            Locale.czech: 'yay',
        },
        name_localizations = {
            Locale.thai: 'nay',
            Locale.czech: 'lay',
        },
        nsfw = True,
        options = [
            ApplicationCommandOption(
                'option',
                'optional',
                ApplicationCommandOptionType.string,

            )
        ],
        required_permissions = Permission().update_by_keys(administrator=True),
        target_type = ApplicationCommandTargetType.chat,
    )
    
    return len(application_command)



def test__ApplicationCommand__len__2():
    """
    Tests whether ``ApplicationCommand.__len__`` only counts the longest description's length and not all's together.
    
    Case: The longest is a localization.
    """
    name = 'owo'
    
    description_1 = 'hi'
    description_2 = 'hoi'
    description_3 = 'halo'
    
    application_command = ApplicationCommand(
        name,
        description_1,
        description_localizations = {
            Locale.thai: description_2,
            Locale.czech: description_3,
        }
    )
    
    expected_length = len(name) + max(
        len(description) for description in (description_1, description_2, description_3)
    )
    
    vampytest.assert_eq(len(application_command), expected_length,)


def test__ApplicationCommand__len__3():
    """
    Tests whether ``ApplicationCommand.__len__`` only counts the longest description's length and not all's together.
    
    Case: The longest is the description itself.
    """
    name = 'owo'
    
    description_1 = 'hi'
    description_2 = 'hoi'
    description_3 = 'halo'
    
    application_command = ApplicationCommand(
        name,
        description_3,
        description_localizations = {
            Locale.thai: description_1,
            Locale.czech: description_2,
        }
    )
    
    expected_length = len(name) + max(
        len(description) for description in (description_1, description_2, description_3)
    )
    
    vampytest.assert_eq(len(application_command), expected_length,)


def test__ApplicationCommand__len__4():
    """
    Tests whether ``ApplicationCommand.__len__`` only counts the longest name's length and not all's together.
    
    Case: The longest is a localization.
    """
    name_1 = 'hi'
    name_2 = 'hoi'
    name_3 = 'halo'
    
    application_command = ApplicationCommand(
        name_1,
        None,
        name_localizations = {
            Locale.thai: name_2,
            Locale.czech: name_3,
        },
        target_type = ApplicationCommandTargetType.user,
    )
    
    expected_length = max(
        len(name) for name in (name_1, name_2, name_3)
    )
    
    vampytest.assert_eq(len(application_command), expected_length,)


def test__ApplicationCommand__len__5():
    """
    Tests whether ``ApplicationCommand.__len__`` only counts the longest name's length and not all's together.
    
    Case: The longest is the name itself.
    """
    name_1 = 'hi'
    name_2 = 'hoi'
    name_3 = 'halo'
    
    application_command = ApplicationCommand(
        name_3,
        None,
        name_localizations = {
            Locale.thai: name_1,
            Locale.czech: name_2,
        },
        target_type = ApplicationCommandTargetType.user,
    )
    
    expected_length = max(
        len(name) for name in (name_1, name_2, name_3)
    )
    
    vampytest.assert_eq(len(application_command), expected_length,)



def test__ApplicationCommand__repr():
    """
    Tests whether ``ApplicationCommand.__repr__`` works as intended.
    """
    application_command = ApplicationCommand(
        'owo',
        'description',
        allow_in_dm = True,
        description_localizations = {
            Locale.thai: 'ayy',
            Locale.czech: 'yay',
        },
        name_localizations = {
            Locale.thai: 'nay',
            Locale.czech: 'lay',
        },
        nsfw = True,
        options = [
            ApplicationCommandOption(
                'option',
                'optional',
                ApplicationCommandOptionType.string,

            )
        ],
        required_permissions = Permission().update_by_keys(administrator=True),
        target_type = ApplicationCommandTargetType.chat,
    )
    
    vampytest.assert_instance(repr(application_command), str)
