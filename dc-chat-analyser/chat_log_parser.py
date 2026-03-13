import json
from typing import Any
from datetime import datetime
from chat_data import Chat, ChatMetadata, Message, User


class ChatLogParser:

    @staticmethod
    def load_chat_log_data(path) -> Any:
        with open(path, 'r', encoding='utf-8') as file:
                data = json.load(file)
                return data
        
    @staticmethod
    def parse_message(message_data) -> Message:
        return Message(
            author = message_data["author"]["nickname"],
            content = message_data["content"],
            timestamp = ChatLogParser.parse_timestamp(message_data["timestamp"])
        )
    
    @staticmethod
    def parse_messages(data) -> list[Message]:
        messages = [ChatLogParser.parse_message(msg_data) for msg_data in data["messages"]]
        return messages

    @staticmethod
    def parse_timestamp(iso: str) -> int:
        dt = datetime.fromisoformat(iso)
        unix = int(dt.timestamp())
        return unix

    @staticmethod
    def parse_user(message_data) -> User:
        return User(
            username = message_data["author"]["name"],
            nickname = message_data["author"]["nickname"],
            avatar_url = message_data["author"]["avatarUrl"]
        )
    
    @staticmethod
    def parse_users(data) -> list[User]:
        users = {}
        for message_data in data["messages"]:
            author_name = message_data["author"]["name"]
            # Ignore bots and deleted users
            if message_data["author"]["isBot"] or author_name == "Deleted User":
                continue

            if author_name not in users.keys():
                user = ChatLogParser.parse_user(message_data)
                users[user.username] = user

            users[message_data["author"]["name"]].messages_sent += 1
            
        return users

    @staticmethod
    def parse_chat_metadata(data) -> ChatMetadata:
        return ChatMetadata(
            guild_name = data["guild"]["name"],
            guild_icon_url = data["guild"]["iconUrl"],
            channel_type = data["channel"]["type"],
            channel_name = data["channel"]["name"]
        )
    
    @staticmethod
    def build_chat_object(path) -> Chat:
        data = ChatLogParser.load_chat_log_data(path)
        return Chat(
                metadata = ChatLogParser.parse_chat_metadata(data),
                messages = ChatLogParser.parse_messages(data),
                users = ChatLogParser.parse_users(data)
        )