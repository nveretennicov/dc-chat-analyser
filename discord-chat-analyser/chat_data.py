from dataclasses import dataclass


@dataclass
class ChatMetadata:
    guild_name : str
    guild_icon_url : str
    channel_type : str
    channel_name : str

@dataclass
class Message:
    author : str
    content : str
    timestamp : int

@dataclass
class User:
    username : str
    nickname : str
    avatar_url : str
    messages_sent : int = 0

@dataclass
class Chat:
    metadata : ChatMetadata
    messages : list[Message]
    users : list[User]