import vampytest

from ..unicode_type import Unicode


def test__Unicode__get_system_name():
    """
    Tests whether ``Unicode``'s `.get_system_name` works as intended.
    """
    name = 'owo'
    unicode = Unicode(name, b'', False, None, None)
    
    system_name = unicode.get_system_name()
    vampytest.assert_instance(system_name, str)
    vampytest.assert_in(name, system_name)


def test__Unicode__iter_emoticons__0():
    """
    Tests whether ``Unicode``'s `.iter_emoticons` works as intended.
    
    Case: 0
    """
    unicode = Unicode('', b'', False, None, None)
    
    vampytest.assert_eq({*unicode.iter_emoticons()}, set())


def test__Unicode__iter_emoticons__1():
    """
    Tests whether ``Unicode``'s `.iter_emoticons` works as intended.
    
    Case: 1+
    """
    emoticons = ('owo', 'uwu')
    unicode = Unicode('', b'', False, None, emoticons)
    
    vampytest.assert_eq({*unicode.iter_emoticons()}, {*emoticons})


def test__Unicode__iter_aliases__0():
    """
    Tests whether ``Unicode``'s `.iter_aliases` works as intended.
    
    Case: 0
    """
    unicode = Unicode('', b'', False, None, None)
    
    vampytest.assert_eq({*unicode.iter_aliases()}, set())


def test__Unicode__iter_aliases__1():
    """
    Tests whether ``Unicode``'s `.iter_aliases` works as intended.
    
    Case: 1+
    """
    aliases = ('owo', 'uwu')
    unicode = Unicode('', b'', False, aliases, None)
    
    vampytest.assert_eq({*unicode.iter_aliases()}, {*aliases})


def test__Unicode__iter_alternative_names__0():
    """
    Tests whether ``Unicode``'s `.iter_alternative_names` works as intended.
    
    Case: 0
    """
    unicode = Unicode('', b'', False, None, None)
    
    vampytest.assert_eq({*unicode.iter_alternative_names()}, set())


def test__Unicode__iter_alternative_names__1():
    """
    Tests whether ``Unicode``'s `.iter_alternative_names` works as intended.
    
    Case: 1+
    """
    emoticons = ('owo', 'uwu')
    aliases = ('awa', 'iwi')
    
    unicode = Unicode('', b'', False, aliases, emoticons)
    
    vampytest.assert_eq({*unicode.iter_alternative_names()}, {*emoticons, *aliases})
