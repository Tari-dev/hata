__all__ = ('import_extension',)

from sys import _getframe as get_frame

from ..extension import EXTENSIONS
from ..extension_loader import EXTENSION_LOADER


def import_extension(extension_name, *variable_names):
    """
    Imports from the given extension.
    
    Parameters
    ----------
    extension_name : `str`
        the extension's name to import.
    
    *variable_names : `str`
        Variables to load from the extension.
        
        > If no variable is defined, the module is returned instead.
    
    Returns
    -------
    imported_variables : `Any`, `list` of `Any`
        The imported variable(s).
    
    Raises
    ------
    ImportError
        - Cannot find the designated extension.
    RuntimeError
        - If called from non extension file.
    TypeError
        - If `extension_name` is not a string.
        - If `variables_to_import` contains a non string.
    ValueError
        - If `extension_name`'s syntax is incorrect.
        - If `variable_names` contains a non identifier.
    ExtensionError
        - Any exception raised by the other extension is funneled.
    """
    # Validate input types
    if not isinstance(extension_name, str):
        raise TypeError(
            f'extension_name` can be `str`, got {extension_name.__class__.__name__}; {extension_name!r}.'
        )
    
    for variable_name in variable_names:
        if not isinstance(variable_name, str):
            raise TypeError(
                f'`variable_names` can contain only `str`, got {extension_name.__class__.__name__}; '
                f'{extension_name!r}; variable_names={variable_names!r}.'
            )
        
        if not variable_name.isidentifier():
            raise ValueError
        
    
    # Validate `extension_name` syntax.
    if not extension_name:
        raise ValueError(
            f'`extension_name`\s syntax is incorrect; Cannot be empty string.'
        )
    
    extension_name_parts = extension_name.split('.')
    expects_only_identifiers = False
    
    for extension_name_part in extension_name_parts:
        if not expects_only_identifiers:
            if not extension_name_part:
                continue
            
            expects_only_identifiers = True
        
        if not extension_name_part:
            raise ValueError(
                f'`extension_name`\s syntax is incorrect; two dot character cannot follow an identifier; got: '
                f'{extension_name!r}.'
            )
        
        if not extension_name_part.isidentifier():
            raise ValueError(
                f'`extension_name`\s syntax is incorrect; {extension_name_part!r} is not an identifier; got: '
                f'{extension_name!r}.'
            )
    
    if not extension_name_parts[-1]:
        raise ValueError(
            f'`extension_name`\s syntax is incorrect; Cannot end with dot character; got: {extension_name!r}.'
        )
    
    # Get local frame and build the extension name to load
    frame = get_frame().f_back
    spec = frame.f_globals.get('__spec__', None)
    if spec is None:
        raise RuntimeError(
            f'`import_extension` can only be called from an extension.'
        )
    
    local_name = spec.name
    
    
    empty_count = 0
    for extension_name_part in extension_name_parts:
        if extension_name_part:
            break
        
        empty_count += 1
        continue
    
    if empty_count:
        local_name_parts = local_name.split('.')
        
        if len(local_name_parts) < empty_count:
            raise ImportError(
                f'`{extension_name!r}`\'s scope out of parent root\'s scope.'
            )
        
        built_name = '.'.join(local_name_parts[:-empty_count] + extension_name_parts[empty_count:])
        
    else:
        built_name = extension_name
    
    try:
        extension = EXTENSION_LOADER.load_extension(built_name)
    except BaseException as err:
        raise
    
    current_extension = EXTENSIONS.get(local_name, None)
    if (current_extension is not None):
        extension.add_child_extension(current_extension)
    
    variable_names_length = len(variable_names)
    module = extension._module
    if variable_names_length == 0:
        return module
    
    variables = []
    
    for variable_name in variable_names:
        try:
            variable = getattr(module, variable_name)
        except AttributeError:
            raise ImportError(
                f'Cannot import `{variable_name}` from `{extension.name}`.'
            ) from None
        
        variables.append(variable)
    
    if variable_names_length == 1:
        return variables[0]
    
    return variables
