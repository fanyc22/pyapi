import MessageType_pb2 as _MessageType_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AttackMsg(_message.Message):
    __slots__ = ["angle", "player_id", "team_id"]
    ANGLE_FIELD_NUMBER: _ClassVar[int]
    PLAYER_ID_FIELD_NUMBER: _ClassVar[int]
    TEAM_ID_FIELD_NUMBER: _ClassVar[int]
    angle: float
    player_id: int
    team_id: int
    def __init__(self, player_id: _Optional[int] = ..., angle: _Optional[float] = ..., team_id: _Optional[int] = ...) -> None: ...

class BuildShipMsg(_message.Message):
    __slots__ = ["birthpoint_index", "ship_type", "team_id"]
    BIRTHPOINT_INDEX_FIELD_NUMBER: _ClassVar[int]
    SHIP_TYPE_FIELD_NUMBER: _ClassVar[int]
    TEAM_ID_FIELD_NUMBER: _ClassVar[int]
    birthpoint_index: int
    ship_type: _MessageType_pb2.ShipType
    team_id: int
    def __init__(self, ship_type: _Optional[_Union[_MessageType_pb2.ShipType, str]] = ..., team_id: _Optional[int] = ..., birthpoint_index: _Optional[int] = ...) -> None: ...

class ConstructMsg(_message.Message):
    __slots__ = ["construction_type", "player_id", "team_id"]
    CONSTRUCTION_TYPE_FIELD_NUMBER: _ClassVar[int]
    PLAYER_ID_FIELD_NUMBER: _ClassVar[int]
    TEAM_ID_FIELD_NUMBER: _ClassVar[int]
    construction_type: _MessageType_pb2.ConstructionType
    player_id: int
    team_id: int
    def __init__(self, player_id: _Optional[int] = ..., construction_type: _Optional[_Union[_MessageType_pb2.ConstructionType, str]] = ..., team_id: _Optional[int] = ...) -> None: ...

class IDMsg(_message.Message):
    __slots__ = ["player_id", "team_id"]
    PLAYER_ID_FIELD_NUMBER: _ClassVar[int]
    TEAM_ID_FIELD_NUMBER: _ClassVar[int]
    player_id: int
    team_id: int
    def __init__(self, player_id: _Optional[int] = ..., team_id: _Optional[int] = ...) -> None: ...

class InstallMsg(_message.Message):
    __slots__ = ["module_type", "player_id", "team_id"]
    MODULE_TYPE_FIELD_NUMBER: _ClassVar[int]
    PLAYER_ID_FIELD_NUMBER: _ClassVar[int]
    TEAM_ID_FIELD_NUMBER: _ClassVar[int]
    module_type: _MessageType_pb2.ModuleType
    player_id: int
    team_id: int
    def __init__(self, module_type: _Optional[_Union[_MessageType_pb2.ModuleType, str]] = ..., player_id: _Optional[int] = ..., team_id: _Optional[int] = ...) -> None: ...

class MoveMsg(_message.Message):
    __slots__ = ["angle", "player_id", "team_id", "time_in_milliseconds"]
    ANGLE_FIELD_NUMBER: _ClassVar[int]
    PLAYER_ID_FIELD_NUMBER: _ClassVar[int]
    TEAM_ID_FIELD_NUMBER: _ClassVar[int]
    TIME_IN_MILLISECONDS_FIELD_NUMBER: _ClassVar[int]
    angle: float
    player_id: int
    team_id: int
    time_in_milliseconds: int
    def __init__(self, player_id: _Optional[int] = ..., angle: _Optional[float] = ..., time_in_milliseconds: _Optional[int] = ..., team_id: _Optional[int] = ...) -> None: ...

class NullRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class PlayerMsg(_message.Message):
    __slots__ = ["player_id", "ship_type", "team_id"]
    PLAYER_ID_FIELD_NUMBER: _ClassVar[int]
    SHIP_TYPE_FIELD_NUMBER: _ClassVar[int]
    TEAM_ID_FIELD_NUMBER: _ClassVar[int]
    player_id: int
    ship_type: _MessageType_pb2.ShipType
    team_id: int
    def __init__(self, player_id: _Optional[int] = ..., team_id: _Optional[int] = ..., ship_type: _Optional[_Union[_MessageType_pb2.ShipType, str]] = ...) -> None: ...

class RecoverMsg(_message.Message):
    __slots__ = ["player_id", "recover", "team_id"]
    PLAYER_ID_FIELD_NUMBER: _ClassVar[int]
    RECOVER_FIELD_NUMBER: _ClassVar[int]
    TEAM_ID_FIELD_NUMBER: _ClassVar[int]
    player_id: int
    recover: int
    team_id: int
    def __init__(self, player_id: _Optional[int] = ..., recover: _Optional[int] = ..., team_id: _Optional[int] = ...) -> None: ...

class SendMsg(_message.Message):
    __slots__ = ["binary_message", "player_id", "team_id", "text_message", "to_player_id"]
    BINARY_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    PLAYER_ID_FIELD_NUMBER: _ClassVar[int]
    TEAM_ID_FIELD_NUMBER: _ClassVar[int]
    TEXT_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    TO_PLAYER_ID_FIELD_NUMBER: _ClassVar[int]
    binary_message: bytes
    player_id: int
    team_id: int
    text_message: str
    to_player_id: int
    def __init__(self, player_id: _Optional[int] = ..., to_player_id: _Optional[int] = ..., text_message: _Optional[str] = ..., binary_message: _Optional[bytes] = ..., team_id: _Optional[int] = ...) -> None: ...
