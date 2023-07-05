__all__ = ('AuditLogChange', )

from scarletio import RichAttributeErrorBaseType


class AuditLogChange(RichAttributeErrorBaseType):
    """
    A change of an ``AuditLogEntry``.
    
    Attributes
    ----------
    after : `Any`
        The changed attribute's new value. Defaults to `None`.
    attribute_name : `str`
        The name of the changed attribute.
    before : `Any`
        The changed attribute's original value. Defaults to `None`.
    
    Notes
    -----
    The value of `before` and `after` depending on the value of `attribute_name`. These are:
    
    +-----------------------------------+-----------------------------------------------------------+
    | Attribute name                    | before / after                                            |
    +===================================+===========================================================+
    | actions                           | `None`, `tuple` of ``AutoModerationAction``               |
    +-----------------------------------+-----------------------------------------------------------+
    | afk_channel_id                    | `None`, `int`                                             |
    +-----------------------------------+-----------------------------------------------------------+
    | afk_timeout                       | `None`, `bool`                                            |
    +-----------------------------------+-----------------------------------------------------------+
    | allow                             | `None`, ``Permission``                                    |
    +-----------------------------------+-----------------------------------------------------------+
    | application_command_id            | `None`, `int`                                             |
    +-----------------------------------+-----------------------------------------------------------+
    | application_id                    | `None`, `int`                                             |
    +-----------------------------------+-----------------------------------------------------------+
    | applied_tag_ids                   | `None`, `tuple` of `int`                                  |
    +-----------------------------------+-----------------------------------------------------------+
    | archived                          | `None`, `bool`                                            |
    +-----------------------------------+-----------------------------------------------------------+
    | auto_archive_duration             | `None`, `int`                                             |
    +-----------------------------------+-----------------------------------------------------------+
    | available                         | `None`, `bool`                                            |
    +-----------------------------------+-----------------------------------------------------------+
    | available_tags                    | `None`, `tuple` of ``ForumTag``                           |
    +-----------------------------------+-----------------------------------------------------------+
    | avatar                            | `None`, ``Icon``                                          |
    +-----------------------------------+-----------------------------------------------------------+
    | banner                            | `None`, ``Icon``                                          |
    +-----------------------------------+-----------------------------------------------------------+
    | bitrate                           | `None`, `int`                                             |
    +-----------------------------------+-----------------------------------------------------------+
    | boost_progress_bar_enabled        | `None`, `bool`                                            |
    +-----------------------------------+-----------------------------------------------------------+
    | channel_id                        | `None`, `int`                                             |
    +-----------------------------------+-----------------------------------------------------------+
    | code                              | `None`, `str`                                             |
    +-----------------------------------+-----------------------------------------------------------+
    | color                             | `None`, ``Color``                                         |
    +-----------------------------------+-----------------------------------------------------------+
    | communication_disabled_until      | `None`, `datetime`                                        |
    +-----------------------------------+-----------------------------------------------------------+
    | content_filter                    | `None`, ``ContentFilterLevel``                            |
    +-----------------------------------+-----------------------------------------------------------+
    | creator_id                        | `None`, `int`                                             |
    +-----------------------------------+-----------------------------------------------------------+
    | default_channel_ids               | `None`, `tuple` of `int`                                  |
    +-----------------------------------+-----------------------------------------------------------+
    | days                              | `None`, `int`                                             |
    +-----------------------------------+-----------------------------------------------------------+
    | deaf                              | `None`, `bool`                                            |
    +-----------------------------------+-----------------------------------------------------------+
    | description                       | `None`, `str`                                             |
    +-----------------------------------+-----------------------------------------------------------+
    | default_message_notification      | `None`, ``MessageNotificationLevel``                      |
    +-----------------------------------+-----------------------------------------------------------+
    | default_forum_layout              | `None`, ``ForumLayout``                                   |
    +-----------------------------------+-----------------------------------------------------------+
    | default_sort_order                | `None`, ``SortOrder``                                     |
    +-----------------------------------+-----------------------------------------------------------+
    | default_thread_auto_archive_after | `None`, `int`                                             |
    +-----------------------------------+-----------------------------------------------------------+
    | default_thread_reaction           | `None`, ``Emoji``                                         |
    +-----------------------------------+-----------------------------------------------------------+
    | default_thread_slowmode           | `None`, `int`                                             |
    +-----------------------------------+-----------------------------------------------------------+
    | deny                              | `None`, ``Permission``                                    |
    +-----------------------------------+-----------------------------------------------------------+
    | discovery_splash                  | `None`, ``Icon``                                          |
    +-----------------------------------+-----------------------------------------------------------+
    | enable_emoticons                  | `None`, `bool`                                            |
    +-----------------------------------+-----------------------------------------------------------+
    | enabled                           | `None`, `bool`                                            |
    +-----------------------------------+-----------------------------------------------------------+
    | end                               | `None`, `datetime`                                        |
    +-----------------------------------+-----------------------------------------------------------+
    | entity_id                         | `None`, `int`                                             |
    +-----------------------------------+-----------------------------------------------------------+
    | entity_metadata                   | `None`, ``ScheduledEventEntityMetadataBase``              |
    +-----------------------------------+-----------------------------------------------------------+
    | entity_type                       | `None`, ``ScheduledEventEntityType``                      |
    +-----------------------------------+-----------------------------------------------------------+
    | event_type                        | `None`, ``AutoModerationEventType``                       |
    +-----------------------------------+-----------------------------------------------------------+
    | excluded_channel_ids              | `None`, `tuple` of `int`                                  |
    +-----------------------------------+-----------------------------------------------------------+
    | excluded_keywords                 | `None`, `tuple` of `str`                                  |
    +-----------------------------------+-----------------------------------------------------------+
    | excluded_role_ids                 | `None`, `tuple` of `int`                                  |
    +-----------------------------------+-----------------------------------------------------------+
    | expire_behavior                   | `None`, `int`                                             |
    +-----------------------------------+-----------------------------------------------------------+
    | expire_grace_period               | `None`, `int`                                             |
    +-----------------------------------+-----------------------------------------------------------+
    | flags                             | `None`, ``ChannelFlag``, ``RoleFlag``                     |
    +-----------------------------------+-----------------------------------------------------------+
    | format                            | `None`, ``StickerFormat``                                 |
    +-----------------------------------+-----------------------------------------------------------+
    | guild_id                          | `None`, `int`                                             |
    +-----------------------------------+-----------------------------------------------------------+
    | hub_type                          | `None`, ``HubType``                                       |
    +-----------------------------------+-----------------------------------------------------------+
    | icon                              | `None`, ``Icon``                                          |
    +-----------------------------------+-----------------------------------------------------------+
    | id                                | `None`, `int`                                             |
    +-----------------------------------+-----------------------------------------------------------+
    | image                             | `None`, ``Icon``                                          |
    +-----------------------------------+-----------------------------------------------------------+
    | in_onboarding                     | `None`, `bool`                                            |
    +-----------------------------------+-----------------------------------------------------------+
    | invitable                         | `None`, `bool`                                            |
    +-----------------------------------+-----------------------------------------------------------+
    | invite_splash                     | `None`, ``Icon``                                          |
    +-----------------------------------+-----------------------------------------------------------+
    | inviter_id                        | `None`, `int`                                             |
    +-----------------------------------+-----------------------------------------------------------+
    | keywords                          | `None`, `tuple` of `str`                                  |
    +-----------------------------------+-----------------------------------------------------------+
    | max_age                           | `None`, `int`                                             |
    +-----------------------------------+-----------------------------------------------------------+
    | max_stage_channel_video_users     | `None`, `int`                                             |
    +-----------------------------------+-----------------------------------------------------------+
    | max_uses                          | `None`, `int`                                             |
    +-----------------------------------+-----------------------------------------------------------+
    | max_voice_channel_video_users     | `None`, `bool`                                            |
    +-----------------------------------+-----------------------------------------------------------+
    | mentionable                       | `None`, `bool`                                            |
    +-----------------------------------+-----------------------------------------------------------+
    | message_notification              | `None`, ``MessageNotificationLevel``                      |
    +-----------------------------------+-----------------------------------------------------------+
    | mfa                               | `None`, ``MFA``                                           |
    +-----------------------------------+-----------------------------------------------------------+
    | mute                              | `None`, `bool`                                            |
    +-----------------------------------+-----------------------------------------------------------+
    | name                              | `None`, `str`                                             |
    +-----------------------------------+-----------------------------------------------------------+
    | nick                              | `None`, `str`                                             |
    +-----------------------------------+-----------------------------------------------------------+
    | nsfw                              | `None`, `bool`                                            |
    +-----------------------------------+-----------------------------------------------------------+
    | nsfw_level                        | `None`, ``NsfwLevel``                                     |
    +-----------------------------------+-----------------------------------------------------------+
    | options                           | `None`, `tuple` of ``OnboardingPromptOption``             |
    +-----------------------------------+-----------------------------------------------------------+
    | owner_id                          | `None`, `int`                                             |
    +-----------------------------------+-----------------------------------------------------------+
    | parent_id                         | `None`, `int`                                             |
    +-----------------------------------+-----------------------------------------------------------+
    | pending                           | `None`, `bool`                                            |
    +-----------------------------------+-----------------------------------------------------------+
    | permission_overwrites             | `None`, `dict` of (`int`, ``PermissionOverwrite``) items  |
    +-----------------------------------+-----------------------------------------------------------+
    | permissions                       | `None`, ``Permission``                                    |
    +-----------------------------------+-----------------------------------------------------------+
    | privacy_level                     | `None`, ``PrivacyLevel``                                  |
    +-----------------------------------+-----------------------------------------------------------+
    | prompts                           | `None`, `tuple` of ``OnboardingPrompt``                   |
    +-----------------------------------+-----------------------------------------------------------+
    | position                          | `None`, `int`                                             |
    +-----------------------------------+-----------------------------------------------------------+
    | public_updates_channel_id         | `None`, `int`                                             |
    +-----------------------------------+-----------------------------------------------------------+
    | regex_patterns                    | `None`, `tuple` of `str`                                  |
    +-----------------------------------+-----------------------------------------------------------+
    | region                            | `None`, ``VoiceRegion``                                   |
    +-----------------------------------+-----------------------------------------------------------+
    | required                          | `None`, `bool`                                            |
    +-----------------------------------+-----------------------------------------------------------+
    | role_ids                          | `None`, `tuple` of `int`                                  |
    +-----------------------------------+-----------------------------------------------------------+
    | roles                             | `None`, `tuple` of ``AuditLogRole``                       |
    +-----------------------------------+-----------------------------------------------------------+
    | rules_channel_id                  | `None`, `int`                                             |
    +-----------------------------------+-----------------------------------------------------------+
    | safety_alerts_channel_id          | `None`, `int`                                             |
    +-----------------------------------+-----------------------------------------------------------+
    | separated                         | `None`, `bool`                                            |
    +-----------------------------------+-----------------------------------------------------------+
    | single_select                     | `None`, `bool`                                            |
    +-----------------------------------+-----------------------------------------------------------+
    | slowmode                          | `None`, `int`                                             |
    +-----------------------------------+-----------------------------------------------------------+
    | sku_ids                           | `None`, `tuple` of `int`                                  |
    +-----------------------------------+-----------------------------------------------------------+
    | start                             | `None`, `datetime`                                        |
    +-----------------------------------+-----------------------------------------------------------+
    | system_channel_flags              | `None`, ``SystemChannelFlag``                             |
    +-----------------------------------+-----------------------------------------------------------+
    | system_channel_id                 | `None`, `int`                                             |
    +-----------------------------------+-----------------------------------------------------------+
    | tags                              | `None`, `frozenset` of `str`                              |
    +-----------------------------------+-----------------------------------------------------------+
    | target_id                         | `None`, `int`                                             |
    +-----------------------------------+-----------------------------------------------------------+
    | target_type                       | `None`, ``PermissionOverwriteTargetType``                 |
    +-----------------------------------+-----------------------------------------------------------+
    | temporary                         | `None`, `bool`                                            |
    +-----------------------------------+-----------------------------------------------------------+
    | timed_out_until                   | `None`, `datetime`                                        |
    +-----------------------------------+-----------------------------------------------------------+
    | topic                             | `None`, `str`                                             |
    +-----------------------------------+-----------------------------------------------------------+
    | trigger_metadata                  | `None`, ``AutoModerationRuleTriggerMetadataBase``         |
    +-----------------------------------+-----------------------------------------------------------+
    | trigger_type                      | `None`, ``AutoModerationRuleTriggerType``                 |
    +-----------------------------------+-----------------------------------------------------------+
    | type                              | `None`, ``ChannelType```, ``OnboardingPromptType``        |
    +-----------------------------------+-----------------------------------------------------------+
    | unicode_emoji                     | `None`, ``Emoji``                                         |
    +-----------------------------------+-----------------------------------------------------------+
    | user_limit                        | `None`, `int`                                             |
    +-----------------------------------+-----------------------------------------------------------+
    | uses                              | `None`, `int`                                             |
    +-----------------------------------+-----------------------------------------------------------+
    | vanity_code                       | `None`, `str`                                             |
    +-----------------------------------+-----------------------------------------------------------+
    | verification_level                | `None`, ``VerificationLevel``                             |
    +-----------------------------------+-----------------------------------------------------------+
    | widget_channel_id                 | `None`, `int`                                             |
    +-----------------------------------+-----------------------------------------------------------+
    | widget_enabled                    | `None`, `bool`                                            |
    +-----------------------------------+-----------------------------------------------------------+
    """
    __slots__ = ('after', 'attribute_name', 'before', )
    
    def __init__(self, attribute_name, before, after):
        """
        Creates a new audit log change instance.
        
        Parameters
        ----------
        attribute_name : `str`
            The name of the changed attribute.
        after : `Any`
            The changed attribute's new value.
        before : `Any`
            The changed attribute's original value.
        """
        self.attribute_name = attribute_name
        self.before = before
        self.after = after
    
    def __repr__(self):
        """Returns the representation of the audit log change."""
        return (
            f'{self.__class__.__name__}('
                f'attribute_name = {self.attribute_name!r}, '
                f'before = {self.before!r}, '
                f'after = {self.after!r}'
            f')'
        )
