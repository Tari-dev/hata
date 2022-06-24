__all__ = ()


import reprlib, warnings
from datetime import datetime
from time import time as time_now

from scarletio import Compound, Theory

from ...activity import ACTIVITY_UNKNOWN, ActivityBase, ActivityCustom
from ...channel import Channel
from ...color import Color
from ...gateway.client_gateway import DiscordGateway, PRESENCE as GATEWAY_OPERATION_CODE_PRESENCE
from ...http import DiscordHTTPClient, VALID_ICON_MEDIA_TYPES, VALID_ICON_MEDIA_TYPES_EXTENDED
from ...oauth2 import Connection
from ...preconverters import preconvert_preinstanced_type
from ...user import PremiumType, Status
from ...utils import datetime_to_timestamp, get_image_media_type, image_to_base64

from ..request_helpers import get_guild_id, get_guild_id_and_channel_id


class ClientEndpoints(Compound):
    http : DiscordHTTPClient
    premium_type : PremiumType
    is_bot : bool
    guild_profiles : dict
    gateway : DiscordGateway
    
    
    @Theory
    def _set_attributes(self, data): ...
    
    
    async def client_edit(self, **keyword_parameters):
        """
        ``Client.client_edit`` is deprecated and will be removed in 2022 December.
        Please use ``.edit`` instead.
        """
        warnings.warn(
            (
                f'`{self.__class__.__name__}.client_edit` is deprecated and will be removed in '
                f'2022 December. Please use `.edit` instead.'
            ),
            FutureWarning
        )
        return await self.edit(**keyword_parameters)
    
    async def edit(
        self, *, avatar=..., banner=..., banner_color=..., bio=..., name=..., # Generic
        password=..., new_password=..., email=..., # User account only
    ):
        """
        Edits the client. Only the provided parameters will be changed. Every parameter what refers to a user
        account is not tested.
        
        This method is a coroutine.
        
        Parameters
        ----------
        avatar : `None`, `bytes-like`, Optional (Keyword only)
            An `'jpg'`, `'png'`, `'webp'` image's raw data. If the client is premium account, then it can be
            `'gif'` as well. By passing `None` you can remove the client's current avatar.
        
        banner : `None`, `bytes-like`, Optional (Keyword only)
            An `'jpg'`, `'png'`, `'webp'`, 'gif'` image's raw data. By passing `None` you can remove the client's
            current avatar.
        
        banner_color : `None`, ``Color``, `int`, Optional (Keyword only)
            The new banner color of the client. By passing it as `None` you can remove the client's current one.
        
        bio : `None`, `str`, Optional (Keyword only)
            The new bio of the client. By passing it as `None`, you can remove the client's current one.
        
        name : `str`, Optional (Keyword only)
            The client's new name.
        
        password : `str`, Optional (Keyword only)
            The actual password of the client.
        
        new_password : `str`, Optional (Keyword only)
            The client's new password.
        
        email : `str`, Optional (Keyword only)
            The client's new email.
        
        Raises
        ------
        TypeError
            - If `avatar` was not given as `None`, neither as `bytes-like`.
            - If `banner` was not given as `None`, neither as `bytes-like`.
        ConnectionError
            No internet connection.
        DiscordException
            If any exception was received from the Discord API.
        AssertionError
            - If `name` was given but not as `str`.
            - If `name`'s length is out of range [2:32].
            - If `avatar`'s type in unsettable for the client.
            - If `password` was not given meanwhile the client is not bot.
            - If `password` was not given as `str`.
            - If `email` was given, but not as `str`.
            - If `new_password` was given, but not as `str`.
            - If `bio` is neither `None` nor `str`.
            - If `bio`'s length is out of range [0:190].
            - if `banner_color` is neither `None` nor `int`.
        
        Notes
        -----
        The method's endpoint has long rate limit reset, so consider using timeout and checking rate limits with
        ``RateLimitProxy``.
        
        The `password`, `new_password` and the `email` parameters are only for user accounts.
        """
        data = {}
        
        
        if (avatar is not ...):
            if avatar is None:
                avatar_data = None
            else:
                if not isinstance(avatar, (bytes, bytearray, memoryview)):
                    raise TypeError(
                        f'`avatar` can be `None`, `bytes-like`, got {avatar.__class__.__name__}; '
                        f'{reprlib.repr(avatar)}.'
                    )
                
                if __debug__:
                    media_type = get_image_media_type(avatar)
                    
                    if self.premium_type.value:
                        valid_icon_media_types = VALID_ICON_MEDIA_TYPES_EXTENDED
                    else:
                        valid_icon_media_types = VALID_ICON_MEDIA_TYPES
                    
                    if media_type not in valid_icon_media_types:
                        raise AssertionError(
                            f'Invalid `avatar` type for the client: {media_type}; got {reprlib.repr(avatar)}.'
                        )
                
                avatar_data = image_to_base64(avatar)
            
            data['avatar'] = avatar_data
        
        
        if (banner is not ...):
            if banner is None:
                banner_data = None
            else:
                if not isinstance(banner, (bytes, bytearray, memoryview)):
                    raise TypeError(
                        f'`banner` can be `None`, `bytes-like`, got {banner.__class__.__name__}; '
                        f'{reprlib.repr(banner)}.'
                    )
                
                if __debug__:
                    media_type = get_image_media_type(banner)
                    
                    if media_type not in VALID_ICON_MEDIA_TYPES_EXTENDED:
                        raise AssertionError(
                            f'Invalid `banner` type for the client: {media_type}; got {reprlib.repr(banner)}.'
                        )
                
                banner_data = image_to_base64(banner)
            
            data['banner'] = banner_data
        
        
        if (banner_color is not ...):
            if __debug__:
                if (banner_color is not None) and (not isinstance(banner_color, int)):
                    raise AssertionError(
                        f'`banner_color` can be `None`, `{Color.__name__}`, `int`, got '
                        f'{banner_color.__name__}; {banner_color!r}.'
                    )
            
            data['accent_color'] = banner_color
        
        
        if (bio is not ...):
            if bio is None:
                bio = ''
            else:
                if __debug__:
                    if not isinstance(bio, str):
                        raise AssertionError(
                            f'`bio` can be `None`, `str`, got {bio.__class__.__name__}; {bio!r}.'
                        )
                    
                    bio_length = len(bio)
                    if bio_length > 190:
                        raise AssertionError(
                            f'`bio` length can be in range [0:190], got {bio_length!r}; {bio!r}.'
                        )
            
            data['bio'] = bio
        
        
        if (name is not ...):
            if __debug__:
                if not isinstance(name, str):
                    raise AssertionError(
                        f'`name` can be `str`, got {name.__class__.__name__}; {name!r}.'
                    )
                
                name_length = len(name)
                if name_length < 2 or name_length > 32:
                    raise AssertionError(
                        f'The length of the name can be in range [2:32], got {name_length}; {name!r}.'
                    )
            
            data['username'] = name
        
        
        if not self.is_bot:
            if __debug__:
                if password is ...:
                    raise AssertionError(
                        f'`password` is must for non bots, got {password!r}.'
                    )
                
                if not isinstance(password, str):
                    raise AssertionError(
                        f'`password` can be `str`, got {password.__class__.__name__}; {password!r}.'
                    )
            
            data['password'] = password
            
            
            if (email is not ...):
                if __debug__:
                    if not isinstance(email, str):
                        raise AssertionError(
                            f'`email` can be `str`, got {email.__class__.__name__}; {email!r}.'
                        )
                
                data['email'] = email
            
            
            if (new_password is not ...):
                if __debug__:
                    if not isinstance(new_password, str):
                        raise AssertionError(
                            f'`new_password` can be `str`, got {new_password.__class__.__name__}; '
                            f'{new_password!r}.'
                        )
                
                data['new_password'] = new_password
        
        
        data = await self.http.client_edit(data)
        self._set_attributes(data)
        
        
        if not self.is_bot:
            self.email = data['email']
            try:
                token = data['token']
            except KeyError:
                pass
            else:
                self.token = token
    
    
    async def client_guild_profile_edit(self, *positional_parameters, **keyword_parameters):
        """
        ``Client.client_guild_profile_edit`` is deprecated and will be removed in 2022 December.
        Please use ``.guild_profile_edit`` instead.
        """
        warnings.warn(
            (
                f'`{self.__class__.__name__}.client_guild_profile_edit` is deprecated and will be removed in '
                f'2022 December. Please use `.guild_profile_edit` instead.'
            ),
            FutureWarning
        )
        return await self.guild_profile_edit(*positional_parameters, **keyword_parameters)
    
    
    async def guild_profile_edit(self, guild, *, nick=..., avatar=..., timed_out_until=..., reason=None):
        """
        Edits the client guild profile in the given guild. Nick and guild specific avatars can be edited on this way.
        
        An extra `reason` is accepted as well, which will show up at the respective guild's audit logs.
        
        This method is a coroutine.
        
        Parameters
        ----------
        guild : `None`, `int`, ``Guild``
            The guild where the client's nickname will be changed. If `guild` is given as `None`, then the function
            returns instantly.
        nick : `None`, `str`, Optional (Keyword only)
            The client's new nickname. Pass it as `None` to remove it. Empty strings are interpreted as `None`.
        avatar : `None`, `bytes-like`, Optional (Keyword only)
            The client's new guild specific avatar.
            
            Can be a `'jpg'`, `'png'`, `'webp'` image's raw data. If the client is premium account, then it can be
            `'gif'` as well. By passing `None` you can remove the client's current avatar.
        
        timed_out_until : `None`, `datetime`, Optional (Keyword only)
            Till when the client is timed out. Pass it as `None` to remove it.
        
        reason : `None`, `str` = `None`, Optional (Keyword only)
            Will show up at the respective guild's audit logs.
        
        Raises
        ------
        TypeError
            - `guild` was not given neither as ``Guild``, `int`.
            - If `avatar` is neither `None` nor `bytes-like`.
        ConnectionError
            No internet connection.
        DiscordException
            If any exception was received from the Discord API.
        AssertionError
            - If the nick's length is out of range [1:32].
            - If the nick was not given neither as `None`, `str`.
            - If `avatar`'s type is incorrect.
            - If `timed_out_until` is neither `None` nor `datetime`.
        """
        # Security debug checks.
        if __debug__:
            if (nick is not None):
                if not isinstance(nick, str):
                    raise AssertionError(
                        f'`nick` can be `None`, `str`, got {nick.__class__.__name__}; {nick!r}.'
                    )
                
                nick_length = len(nick)
                if nick_length > 32:
                    raise AssertionError(
                        f'`nick` length can be in range [1:32], got {nick_length}; {nick!r}.'
                    )
                
                # Translate empty nick to `None`
                if nick_length == 0:
                    nick = None
        else:
            # Non debug mode: Translate empty nick to `None`
            if (nick is not None) and (not nick):
                nick = None
        
        
        # Check whether we should edit the nick.
        if guild is None:
            # `guild` can be `None` if `guild` parameter was given as `int`.
            should_edit_nick = True
        else:
            try:
                guild_profile = self.guild_profiles[guild.id]
            except KeyError:
                # we aren't at the guild probably ->  will raise the request for us, if really
                should_edit_nick = True
            else:
                should_edit_nick = (guild_profile.nick != nick)
        
        data = {}
        
        if should_edit_nick:
            data['nick'] = nick
        
        if (avatar is not ...):
            if avatar is None:
                avatar_data = None
            else:
                if not isinstance(avatar, (bytes, bytearray, memoryview)):
                    raise TypeError(
                        f'`avatar` can be `None`, `bytes-like`, got {avatar.__class__.__name__}; '
                        f'{reprlib.repr(avatar)}.'
                    )
                
                if __debug__:
                    media_type = get_image_media_type(avatar)
                    
                    if self.premium_type.value:
                        valid_icon_media_types = VALID_ICON_MEDIA_TYPES_EXTENDED
                    else:
                        valid_icon_media_types = VALID_ICON_MEDIA_TYPES
                    
                    if media_type not in valid_icon_media_types:
                        raise AssertionError(
                            f'Invalid `avatar` type for the client: {media_type}, got {reprlib.repr(avatar)}.'
                        )
                
                avatar_data = image_to_base64(avatar)
            
            data['avatar'] = avatar_data
        
        if (timed_out_until is not ...):
            if timed_out_until is None:
                timed_out_until_raw = None
            else:
                if __debug__:
                    if not isinstance(timed_out_until, datetime):
                        raise AssertionError(
                            f'`timed_out_until` can be `None`, `datetime`, got {timed_out_until.__class__.__name__}; '
                            f'{timed_out_until!r}.'
                        )
                
                timed_out_until_raw = datetime_to_timestamp(timed_out_until)
            
            data['communication_disabled_until'] = timed_out_until_raw
        
        if data:
            await self.http.client_guild_profile_edit(guild_id, data, reason)
    
    
    async def client_connection_get_all(self):
        """
        ``Client.client_connection_get_all`` is deprecated and will be removed in 2022 December.
        Please use ``.connection_get_all`` instead.
        """
        warnings.warn(
            (
                f'`{self.__class__.__name__}.client_connection_get_all` is deprecated and will be removed in '
                f'2022 December. Please use `.connection_get_all` instead.'
            ),
            FutureWarning
        )
        return await self.connection_get_all()
    
    
    async def connection_get_all(self):
        """
        Requests the client's connections.
        
        This method is a coroutine.
        
        Returns
        -------
        connections : `list` of ``Connection`` objects
        
        Raises
        ------
        ConnectionError
            No internet connection.
        DiscordException
            If any exception was received from the Discord API.
        
        Notes
        -----
        For a bot account this request will always return an empty list.
        """
        data = await self.http.client_connection_get_all()
        return [Connection(connection_data) for connection_data in data]
    
    
    async def edit_presence(self, *, activity=..., status=..., afk=False):
        """
        Changes the client's presence (status and activity). If a parameter is not defined, it will not be changed.
        
        This method is a coroutine.
        
        Parameters
        ----------
        activity : ``ActivityBase``, Optional (Keyword only)
            The new activity of the Client.
        status : `str`, ``Status``, Optional (Keyword only)
            The new status of the client.
        afk : `bool` = `False`, Optional (Keyword only)
            Whether the client is afk or not (?).
        
        Raises
        ------
        TypeError:
            - If the status is not `str`, ``Status``.
            - If activity is not ``ActivityBase``, except ``ActivityCustom``.
        ValueError:
            - If the status `str`, but not any of the predefined ones.
        AssertionError
            - If `afk` was not given as `bool`.
        
        Notes
        -----
        This method is an alternative version of ``.client_edit_presence`` till further decision.
        """
        if status is ...:
            status = self._status
        else:
            status = preconvert_preinstanced_type(status, 'status', Status)
            self._status = status
        
        status = status.value
        
        if activity is ...:
            activity = self._activity
        elif activity is None:
            self._activity = ACTIVITY_UNKNOWN
        elif isinstance(activity, ActivityBase) and (not isinstance(activity, ActivityCustom)):
            self._activity = activity
        else:
            raise TypeError(
                f'`activity` can be `{ActivityBase.__name__}` (except `{ActivityCustom.__name__}`), got: '
                f'{activity.__class__.__name__}; {activity!r}.'
            )
        
        if activity is None:
            pass
        elif activity is ACTIVITY_UNKNOWN:
            activity = None
        else:
            if self.is_bot:
                activity = activity.bot_dict()
            else:
                activity = activity.user_dict()
        
        if status == 'idle':
            since = int(time_now() * 1000.)
        else:
            since = 0
        
        if __debug__:
            if not isinstance(afk, bool):
                raise AssertionError(
                    f'`afk` can be `bool`, got {afk.__class__.__name__}; {afk!r}.'
                )
        
        data = {
            'op': GATEWAY_OPERATION_CODE_PRESENCE,
            'd': {
                'game': activity,
                'since': since,
                'status': status,
                'afk': afk,
            },
        }
        
        await self.gateway.send_as_json(data)
    
    
    async def client_edit_presence(self, **keyword_parameters):
        """
        ``Client.client_edit_presence`` is deprecated and will be removed in 2022 December.
        Please use ``.edit_presence`` instead.
        """
        warnings.warn(
            (
                f'`{self.__class__.__name__}.client_edit_presence` is deprecated and will be removed in 2022 December. '
                f'Please use `.edit_presence` instead.'
            ),
            FutureWarning
        )
        
        return await self.edit_presence(**keyword_parameters)
    
    
    async def guild_leave(self, guild):
        """
        The client leaves the given guild.
        
        This method is a coroutine.
        
        Parameters
        ----------
        guild : ``Guild``, `int`
            The guild from where the client will leave.
        
        Raises
        ------
        TypeError
            If `guild` was not given neither as ``Guild`` nor `int`.
        ConnectionError
            No internet connection.
        DiscordException
            If any exception was received from the Discord API.
        """
        guild_id = get_guild_id(guild)
        
        await self.http.guild_leave(guild_id)


    async def join_speakers(self, channel, *, request=False):
        """
        Request to speak or joins the client as a speaker inside of a stage channel. The client must be in the stage
        channel.
        
        This method is a coroutine.
        
        Parameters
        ----------
        channel : ``Channel``
            The stage channel to join.
        request : `bool` = `False`, Optional (Keyword only)
            Whether the client should only request to speak.
        
        Raises
        ------
        TypeError
            If `channel` was not given neither as ``Channel`` nor as `tuple` (`int`, `int`).
        ConnectionError
            No internet connection.
        DiscordException
            If any exception was received from the Discord API.
        """
        guild_id, channel_id = get_guild_id_and_channel_id(channel, Channel.is_guild_stage)
        
        if request:
            timestamp = datetime_to_timestamp(datetime.utcnow())
        else:
            timestamp = None
        
        data = {
            'suppress': False,
            'request_to_speak_timestamp': timestamp,
            'channel_id': channel_id
        }
        
        await self.http.voice_state_client_edit(guild_id, data)
    
    
    async def join_audience(self, channel):
        """
        Moves the client to the audience inside of the stage channel. The client must be in the stage channel.
        
        This method is a coroutine.
        
        Parameters
        ----------
        channel : ``Channel``, `tuple` (`int`, `int`)
            The stage channel to join.
        
        Raises
        ------
        RuntimeError
            If `channel` is partial.
        TypeError
            If `channel` was not given neither as ``Channel`` nor as `tuple` (`int`, `int`).
        ConnectionError
            No internet connection.
        DiscordException
            If any exception was received from the Discord API.
        """
        guild_id, channel_id = get_guild_id_and_channel_id(channel, Channel.is_guild_stage)
        
        data = {
            'suppress': True,
            'channel_id': channel_id
        }
        
        await self.http.voice_state_client_edit(guild_id, data)
