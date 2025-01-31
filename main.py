from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional
import uuid

@dataclass
class User:
    id: uuid.UUID
    name: str
    login: str
    password: str
    chats: List['Chat']

@dataclass
class Chat:
    id: uuid.UUID
    name: str
    messages: List['Message']
    users: List[User]

@dataclass
class Message:
    id: uuid.UUID
    text: str
    datetime: datetime
    owner: User
    chat: Chat

# DTO Classes
@dataclass
class CreateMessageDTO:
    text: str
    user_id: uuid.UUID
    chat_id: uuid.UUID

@dataclass
class CreateChatDTO:
    name: str
    user_id: uuid.UUID

@dataclass
class RegisterUserDTO:
    login: str
    password: str

@dataclass
class LoginUserDTO:
    login: str
    password: str

@dataclass
class GetMessageDTO:
    text: str
    datetime: datetime
    user_name: str

@dataclass
class GetAndLinkChatDTO:
    id: uuid.UUID
    name: str
    messages: List[GetMessageDTO]
    user_names: List[str]

@dataclass
class GetForListChatDTO:
    id: uuid.UUID
    name: str

@dataclass
class GetAccountUserDTO:
    name: str
    chats: List[GetForListChatDTO]

class MessageRepo:
    def create(self, dto: CreateMessageDTO) -> None:
        pass
    
    def read(self, id: uuid.UUID): 
        return GetMessageDTO

class LinkRepo:
    def create(self, dto: CreateChatDTO) -> None:
        pass
    
    def read_and_link(self, user_id: uuid.UUID, chat_id: uuid.UUID):
        return GetAndLinkChatDTO
    
    def read_for_list(self, id: uuid.UUID): 
        return GetForListChatDTO
    
    def register(self, dto: RegisterUserDTO) -> None:
        pass
    
    def login(self, dto: LoginUserDTO):
        return User
    
    def read(self, id: uuid.UUID):
        return GetAccountUserDTO