import vampytest

from ....core import BUILTIN_EMOJIS

from ...forum_tag import ForumTag
from ...permission_overwrite import PermissionOverwrite, PermissionOverwriteTargetType

from ..flags import ChannelFlag
from ..guild_forum import ChannelMetadataGuildForumBase
from ..preinstanced import ForumLayout, SortOrder

from .test__ChannelMetadataGuildForumBase__constructor import _assert_fields_set


def test__ChannelMetadataGuildForumBase__copy():
    """
    Tests whether ``ChannelMetadataGuildForumBase.copy` works as intended.
    """
    name = 'alice'
    parent_id = 202304120157
    permission_overwrites = [
        PermissionOverwrite(202304120158, target_type = PermissionOverwriteTargetType.user)
    ]
    position = 7
    available_tags = [
        ForumTag.precreate(
            202304120159,
            emoji = BUILTIN_EMOJIS['heart'],
            name = 'Yup',
            moderated = False,
        )
    ]
    default_thread_auto_archive_after = 86400
    default_thread_reaction = BUILTIN_EMOJIS['monkey']
    default_thread_slowmode = 60
    flags = ChannelFlag(1)
    topic = 'Dearest'
    default_sort_order = SortOrder.creation_date
    default_forum_layout = ForumLayout.list
    
    channel_metadata = ChannelMetadataGuildForumBase(
        name = name,
        parent_id = parent_id,
        permission_overwrites = permission_overwrites,
        position = position,
        available_tags = available_tags,
        default_thread_auto_archive_after = default_thread_auto_archive_after,
        default_thread_reaction = default_thread_reaction,
        default_thread_slowmode = default_thread_slowmode,
        flags = flags,
        topic = topic,
        default_sort_order = default_sort_order,
        default_forum_layout = default_forum_layout,
    )
    
    copy = channel_metadata.copy()
    _assert_fields_set(copy)
    vampytest.assert_is_not(copy, channel_metadata)
    
    vampytest.assert_eq(copy, channel_metadata)


def test__ChannelMetadataGuildForumBase__copy_with__0():
    """
    Tests whether ``ChannelMetadataGuildForumBase.copy_with` works as intended.
    
    Case: No fields.
    """
    name = 'alice'
    parent_id = 202304120160
    permission_overwrites = [
        PermissionOverwrite(202304120161, target_type = PermissionOverwriteTargetType.user)
    ]
    position = 7
    available_tags = [
        ForumTag.precreate(
            202304120162,
            emoji = BUILTIN_EMOJIS['heart'],
            name = 'Yup',
            moderated = False,
        )
    ]
    default_thread_auto_archive_after = 86400
    default_thread_reaction = BUILTIN_EMOJIS['monkey']
    default_thread_slowmode = 60
    flags = ChannelFlag(1)
    topic = 'Dearest'
    default_sort_order = SortOrder.creation_date
    default_forum_layout = ForumLayout.list
    
    channel_metadata = ChannelMetadataGuildForumBase(
        name = name,
        parent_id = parent_id,
        permission_overwrites = permission_overwrites,
        position = position,
        available_tags = available_tags,
        default_thread_auto_archive_after = default_thread_auto_archive_after,
        default_thread_reaction = default_thread_reaction,
        default_thread_slowmode = default_thread_slowmode,
        flags = flags,
        topic = topic,
        default_sort_order = default_sort_order,
        default_forum_layout = default_forum_layout,
    )
    
    copy = channel_metadata.copy_with()
    _assert_fields_set(copy)
    vampytest.assert_is_not(copy, channel_metadata)
    
    vampytest.assert_eq(copy, channel_metadata)


def test__ChannelMetadataGuildForumBase__copy_with__1():
    """
    Tests whether ``ChannelMetadataGuildForumBase.copy_with` works as intended.
    
    Case: All fields.
    """
    old_name = 'alice'
    old_parent_id = 202304120163
    old_permission_overwrites = [
        PermissionOverwrite(202304120164, target_type = PermissionOverwriteTargetType.user)
    ]
    old_position = 7
    old_available_tags = [
        ForumTag.precreate(
            202304120165,
            emoji = BUILTIN_EMOJIS['heart'],
            name = 'Yup',
            moderated = False,
        )
    ]
    old_default_thread_auto_archive_after = 86400
    old_default_thread_reaction = BUILTIN_EMOJIS['monkey']
    old_default_thread_slowmode = 60
    old_flags = ChannelFlag(1)
    old_topic = 'Dearest'
    old_default_sort_order = SortOrder.creation_date
    old_default_forum_layout = ForumLayout.list
    
    new_name = 'emotion'
    new_parent_id = 202304120166
    new_permission_overwrites = [
        PermissionOverwrite(202304120167, target_type = PermissionOverwriteTargetType.role)
    ]
    new_position = 5
    new_available_tags = [
        ForumTag.precreate(
            202304120168,
            emoji = BUILTIN_EMOJIS['duck'],
            name = 'Ashy',
            moderated = True,
        )
    ]
    new_default_thread_auto_archive_after = 3600
    new_default_thread_reaction = BUILTIN_EMOJIS['radio']
    new_default_thread_slowmode = 600
    new_flags = ChannelFlag(4)
    new_topic = 'My'
    new_default_sort_order = SortOrder.latest_activity
    new_default_forum_layout = ForumLayout.gallery
    
    channel_metadata = ChannelMetadataGuildForumBase(
        name = old_name,
        parent_id = old_parent_id,
        permission_overwrites = old_permission_overwrites,
        position = old_position,
        available_tags = old_available_tags,
        default_thread_auto_archive_after = old_default_thread_auto_archive_after,
        default_thread_reaction = old_default_thread_reaction,
        default_thread_slowmode = old_default_thread_slowmode,
        flags = old_flags,
        topic = old_topic,
        default_sort_order = old_default_sort_order,
        default_forum_layout = old_default_forum_layout,
    )
    
    copy = channel_metadata.copy_with(
        name = new_name,
        parent_id = new_parent_id,
        permission_overwrites = new_permission_overwrites,
        position = new_position,
        available_tags = new_available_tags,
        default_thread_auto_archive_after = new_default_thread_auto_archive_after,
        default_thread_reaction = new_default_thread_reaction,
        default_thread_slowmode = new_default_thread_slowmode,
        flags = new_flags,
        topic = new_topic,
        default_sort_order = new_default_sort_order,
        default_forum_layout = new_default_forum_layout,
    )
    _assert_fields_set(copy)
    vampytest.assert_is_not(copy, channel_metadata)
    
    vampytest.assert_eq(copy.name, new_name)
    vampytest.assert_eq(copy.parent_id, new_parent_id)
    vampytest.assert_eq(
        copy.permission_overwrites,
        {permission_overwrite.target_id: permission_overwrite for permission_overwrite in new_permission_overwrites},
    )
    vampytest.assert_eq(copy.position, new_position)
    vampytest.assert_eq(copy.available_tags, tuple(new_available_tags))
    vampytest.assert_eq(copy.default_thread_auto_archive_after, new_default_thread_auto_archive_after)
    vampytest.assert_eq(copy.default_thread_reaction, new_default_thread_reaction)
    vampytest.assert_eq(copy.default_thread_slowmode, new_default_thread_slowmode)
    vampytest.assert_eq(copy.flags, new_flags)
    vampytest.assert_eq(copy.topic, new_topic)
    vampytest.assert_is(copy.default_sort_order, new_default_sort_order)
    vampytest.assert_is(copy.default_forum_layout, new_default_forum_layout)



def test__ChannelMetadataGuildForumBase__copy_with_keyword_parameters__0():
    """
    Tests whether ``ChannelMetadataGuildForumBase.copy_with_keyword_parameters` works as intended.
    
    Case: No fields.
    """
    name = 'alice'
    parent_id = 202304120169
    permission_overwrites = [
        PermissionOverwrite(202304120170, target_type = PermissionOverwriteTargetType.user)
    ]
    position = 7
    available_tags = [
        ForumTag.precreate(
            202304120171,
            emoji = BUILTIN_EMOJIS['heart'],
            name = 'Yup',
            moderated = False,
        )
    ]
    default_thread_auto_archive_after = 86400
    default_thread_reaction = BUILTIN_EMOJIS['monkey']
    default_thread_slowmode = 60
    flags = ChannelFlag(1)
    topic = 'Dearest'
    default_sort_order = SortOrder.creation_date
    default_forum_layout = ForumLayout.list
    
    channel_metadata = ChannelMetadataGuildForumBase(
        name = name,
        parent_id = parent_id,
        permission_overwrites = permission_overwrites,
        position = position,
        available_tags = available_tags,
        default_thread_auto_archive_after = default_thread_auto_archive_after,
        default_thread_reaction = default_thread_reaction,
        default_thread_slowmode = default_thread_slowmode,
        flags = flags,
        topic = topic,
        default_sort_order = default_sort_order,
        default_forum_layout = default_forum_layout,
    )
    
    keyword_parameters = {}
    copy = channel_metadata.copy_with_keyword_parameters(keyword_parameters)
    _assert_fields_set(copy)
    vampytest.assert_is_not(copy, channel_metadata)
    vampytest.assert_eq(keyword_parameters, {})
    
    vampytest.assert_eq(copy, channel_metadata)


def test__ChannelMetadataGuildForumBase__copy_with_keyword_parameters__1():
    """
    Tests whether ``ChannelMetadataGuildForumBase.copy_with_keyword_parameters` works as intended.
    
    Case: All fields.
    """
    old_name = 'alice'
    old_parent_id = 202304120172
    old_permission_overwrites = [
        PermissionOverwrite(202304120173, target_type = PermissionOverwriteTargetType.user)
    ]
    old_position = 7
    old_available_tags = [
        ForumTag.precreate(
            202304120174,
            emoji = BUILTIN_EMOJIS['heart'],
            name = 'Yup',
            moderated = False,
        )
    ]
    old_default_thread_auto_archive_after = 86400
    old_default_thread_reaction = BUILTIN_EMOJIS['monkey']
    old_default_thread_slowmode = 60
    old_flags = ChannelFlag(1)
    old_topic = 'Dearest'
    old_default_sort_order = SortOrder.creation_date
    old_default_forum_layout = ForumLayout.list
    
    new_name = 'emotion'
    new_parent_id = 202304120175
    new_permission_overwrites = [
        PermissionOverwrite(202304120176, target_type = PermissionOverwriteTargetType.role)
    ]
    new_position = 5
    new_available_tags = [
        ForumTag.precreate(
            202304120177,
            emoji = BUILTIN_EMOJIS['duck'],
            name = 'Ashy',
            moderated = True,
        )
    ]
    new_default_thread_auto_archive_after = 3600
    new_default_thread_reaction = BUILTIN_EMOJIS['radio']
    new_default_thread_slowmode = 600
    new_flags = ChannelFlag(4)
    new_topic = 'My'
    new_default_sort_order = SortOrder.latest_activity
    new_default_forum_layout = ForumLayout.gallery
    
    channel_metadata = ChannelMetadataGuildForumBase(
        name = old_name,
        parent_id = old_parent_id,
        permission_overwrites = old_permission_overwrites,
        position = old_position,
        available_tags = old_available_tags,
        default_thread_auto_archive_after = old_default_thread_auto_archive_after,
        default_thread_reaction = old_default_thread_reaction,
        default_thread_slowmode = old_default_thread_slowmode,
        flags = old_flags,
        topic = old_topic,
        default_sort_order = old_default_sort_order,
        default_forum_layout = old_default_forum_layout,
    )
    
    keyword_parameters = {
        'name': new_name,
        'parent_id': new_parent_id,
        'permission_overwrites': new_permission_overwrites,
        'position': new_position,
        'available_tags': new_available_tags,
        'default_thread_auto_archive_after': new_default_thread_auto_archive_after,
        'default_thread_reaction': new_default_thread_reaction,
        'default_thread_slowmode': new_default_thread_slowmode,
        'flags': new_flags,
        'topic': new_topic,
        'default_sort_order': new_default_sort_order,
        'default_forum_layout': new_default_forum_layout,
    }
    
    copy = channel_metadata.copy_with_keyword_parameters(keyword_parameters)
    _assert_fields_set(copy)
    vampytest.assert_is_not(copy, channel_metadata)
    vampytest.assert_eq(keyword_parameters, {})
    
    vampytest.assert_eq(copy.name, new_name)
    vampytest.assert_eq(copy.parent_id, new_parent_id)
    vampytest.assert_eq(
        copy.permission_overwrites,
        {permission_overwrite.target_id: permission_overwrite for permission_overwrite in new_permission_overwrites},
    )
    vampytest.assert_eq(copy.position, new_position)
    vampytest.assert_eq(copy.available_tags, tuple(new_available_tags))
    vampytest.assert_eq(copy.default_thread_auto_archive_after, new_default_thread_auto_archive_after)
    vampytest.assert_eq(copy.default_thread_reaction, new_default_thread_reaction)
    vampytest.assert_eq(copy.default_thread_slowmode, new_default_thread_slowmode)
    vampytest.assert_eq(copy.flags, new_flags)
    vampytest.assert_eq(copy.topic, new_topic)
    vampytest.assert_is(copy.default_sort_order, new_default_sort_order)
    vampytest.assert_is(copy.default_forum_layout, new_default_forum_layout)
