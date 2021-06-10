__all__ = ('SlashCommandError', 'SlashCommandParameterConversionError')

from ...backend.utils import copy_docs
from ...backend.export import include

from ...discord.interaction import InteractionType
from ...discord.exceptions import DiscordException, ERROR_CODES

SlashCommand = include('SlashCommand')

class SlashCommandError(Exception):
    """
    Base class for slash command internal errors.
    """
    pass

    @property
    def pretty_repr(self):
        """
        Returns the pretty representation of the exception.
        
        Returns
        -------
        representation : `str`
        """
        return ''

class SlashCommandParameterConversionError(SlashCommandError):
    """
    Exception raised when a command's parameter's parsing fails.
    
    Attributes
    ----------
    _pretty_repr : `None` or `str`
        generated pretty representation of the exception.
    _repr : `None` or `str`
        The generated error message.
    parameter_name : `str` or `None`
        The parameter's name, which failed to be parsed.
    received_value : `str` or `None`
        The parameter's received value.
    excepted_type : `str` or `None`
        The parameter's expected type's name.
    expected_values : `None` or `list` of `Any`
        Expected values.
    """
    def __init__(self, parameter_name, received_value, excepted_type, expected_values):
        """
        Creates a new ``SlashCommandParameterConversionError`` instance with the given parameters.
        
        Parameters
        ----------
        parameter_name : `str` or `None`
            The parameter's name, which failed to be parsed.
        received_value : `str` or `None`
            The parameter's received value.
        excepted_type : `str` or `None`
            The parameter's expected type's name.
        expected_values : `None` or `list` of `Any`
            Expected values.
        """
        self.parameter_name = parameter_name
        self.received_value = received_value
        self.excepted_type = excepted_type
        self.expected_values = expected_values
        self._repr = None
        self._pretty_repr = None
        Exception.__init__(self, parameter_name, received_value, excepted_type, expected_values)
    
    def __repr__(self):
        """Returns the representation of the parameter conversion error."""
        repr_ = self._repr
        if repr_ is None:
            repr_ = self._create_repr()
        
        return repr_

    def _create_repr(self):
        """
        Creates the representation of the parsing syntax error.
        
        Returns
        -------
        repr_ : `str`
            The representation of the syntax error.
        """
        repr_parts = [self.__class__.__name__]
        
        parameter_name = self.parameter_name
        if (parameter_name is not None):
            repr_parts.append('\n')
            repr_parts.append('parameter name: ')
            repr_parts.append(repr(parameter_name))
        
        excepted_type = self.excepted_type
        if (excepted_type is not None):
            repr_parts.append(
                '\n'
                'expected type: '
            )
            repr_parts.append(excepted_type)
        
        expected_values = self.expected_values
        if (expected_values is not None):
            repr_parts.append(
                '\n'
                'expected value(s):'
            )
            
            index = 0
            limit = len(expected_values)
            while True:
                value = expected_values[index]
                index += 1
                
                repr_parts.append(repr(value))
                if index == limit:
                    break
                
                repr_parts.append(', ')
                continue
        
        repr_parts.append(
            '\n'
            'received value: '
        )
        received_value = self.received_value
        if (received_value is None):
            repr_parts.append('N/A')
        else:
            repr_parts.append(repr(received_value))
        
        repr_ = ''.join(repr_parts)
        self._repr = repr_
        return repr_
    
    
    @property
    @copy_docs(SlashCommandError.pretty_repr)
    def pretty_repr(self):
        pretty_repr = self._pretty_repr
        if pretty_repr is None:
            pretty_repr = self._create_pretty_repr()
        
        return pretty_repr
    
    
    def _create_pretty_repr(self):
        """
        Creates the pretty representation of the parameter conversion error.
        
        Returns
        -------
        repr_ : `str`
            The representation of the parameter conversion error.
        """
        repr_parts = ['Parameter conversion failed\n']
        
        parameter_name = self.parameter_name
        if (parameter_name is not None):
            repr_parts.append('\n')
            repr_parts.append('Name: `')
            repr_parts.append(parameter_name)
            repr_parts.append('`')
        
        excepted_type = self.excepted_type
        if (excepted_type is not None):
            repr_parts.append(
                '\n'
                'Excepted type: `'
            )
            repr_parts.append(excepted_type)
            repr_parts.append('`')
    
        
        expected_values = self.expected_values
        if (expected_values is not None):
            repr_parts.append(
                '\n'
                'Expected value(s):'
            )
            
            for expected_value in expected_values:
                repr_parts.append('\n- `')
                repr_parts.append(expected_value)
                repr_parts.append('`')
        
        repr_parts.append(
            '\n'
            'Received: '
        )
        received_value = self.received_value
        if (received_value is None):
            repr_parts.append('N/A')
        else:
            repr_parts.append('`')
            repr_parts.append(received_value)
            repr_parts.append('`')
        
        pretty_repr = ''.join(repr_parts)
        self._pretty_repr = pretty_repr
        return pretty_repr


async def _default_slasher_exception_handler(client, interaction_event, command, exception):
    """
    Default ``Slasher`` exception handler.
    
    This function is a coroutine.
    
    Parameters
    ----------
    client : ``Client``
        The respective client.
    interaction_event : ``InteractionEvent``
        The received interaction event.
    command : ``SlashCommand`` or ``ComponentCommand``
        The command, which raised.
    exception : `BaseException`
        The occurred exception.
    
    Returns
    -------
    handled : `bool`
        Whether the error handler handled the exception.
    """
    if isinstance(exception, SlashCommandError):
        forward = exception.pretty_repr
        render = False
    elif (interaction_event.type is InteractionType.application_command) and (not interaction_event.responded()):
        forward = (
           'Exception occurred meanwhile processing your interaction.\n'
           'Our highly educated Cirno-s are already working on the problem.'
        )
        render = True
    else:
        forward = None
        render = True
    
    if (forward is not None):
        try:
            await client.interaction_response_message_create(interaction_event, forward, show_for_invoking_user_only=True)
        except BaseException as err:
            if isinstance(err, ConnectionError):
                pass
            elif isinstance(err, DiscordException) and (err.code == ERROR_CODES.unknown_interaction):
                pass
            else:
                raise
    
    if render:
        if isinstance(command, SlashCommand):
            command_name = command.name
        else:
            command_name = command.__class__.__name__
        
        await client.events.error(client, f'`Slasher` while calling `{command_name}', exception)
    
    return True
