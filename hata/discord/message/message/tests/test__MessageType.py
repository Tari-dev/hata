from datetime import datetime as DateTime
from types import FunctionType

import vampytest

from ....user import User

from ..message import Message
from ..preinstanced import MessageType

from ...message_call import MessageCall


def test__MessageType__name():
    """
    Tests whether ``MessageType`` instance names are all strings.
    """
    for instance in MessageType.INSTANCES.values():
        vampytest.assert_instance(instance.name, str)


def test__MessageType__value():
    """
    Tests whether ``MessageType`` instance values are all the expected value type.
    """
    for instance in MessageType.INSTANCES.values():
        vampytest.assert_instance(instance.value, MessageType.VALUE_TYPE)


def test__MessageType__converter():
    """
    Tests whether ``MessageType`` converters are all the expected value type.
    """
    for instance in MessageType.INSTANCES.values():
        vampytest.assert_instance(instance.converter, FunctionType)


def test__MessageType__deletable():
    """
    Tests whether ``MessageType.deletable``-s are all set as expected.
    """
    for instance in MessageType.INSTANCES.values():
        vampytest.assert_instance(instance.deletable, bool)


def test__MessageType__call():
    """
    Tests whether ``MessageType.call`` conversion not fails.
    """
    ended_at = DateTime(2016, 4, 4)
    user_0 = User.precreate(202305060000)
    user_1 = User.precreate(202305060001)
    
    for message in (
        Message(),
        Message(author = user_0),
        Message(author = user_0, call = MessageCall()),
        Message(author = user_0, call = MessageCall(ended_at = ended_at)),
        Message(author = user_0, call = MessageCall(user_ids = [user_0.id])),
        Message(author = user_0, call = MessageCall(user_ids = [user_0.id, user_1.id])),
        Message(author = user_0, call = MessageCall(ended_at = ended_at, user_ids = [user_0.id, user_1.id])),
    ):
        output = MessageType.call.converter(message)
        vampytest.assert_instance(output, str, nullable = True)
