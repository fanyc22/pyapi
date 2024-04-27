import MessageType_pb2 as _MessageType_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BoolRes(_message.Message):
    __slots__ = ["act_success"]
    ACT_SUCCESS_FIELD_NUMBER: _ClassVar[int]
    act_success: bool
    def __init__(self, act_success: bool = ...) -> None: ...

class BuildShipRes(_message.Message):
    __slots__ = ["act_success", "player_id"]
    ACT_SUCCESS_FIELD_NUMBER: _ClassVar[int]
    PLAYER_ID_FIELD_NUMBER: _ClassVar[int]
    act_success: bool
    player_id: int
    def __init__(self, act_success: bool = ..., player_id: _Optional[int] = ...) -> None: ...

class EcoRes(_message.Message):
    __slots__ = ["economy"]
    ECONOMY_FIELD_NUMBER: _ClassVar[int]
    economy: int
    def __init__(self, economy: _Optional[int] = ...) -> None: ...

class MessageOfAll(_message.Message):
    __slots__ = ["blue_home_hp", "blue_team_energy", "blue_team_score", "game_time", "red_home_hp", "red_team_energy", "red_team_score"]
    BLUE_HOME_HP_FIELD_NUMBER: _ClassVar[int]
    BLUE_TEAM_ENERGY_FIELD_NUMBER: _ClassVar[int]
    BLUE_TEAM_SCORE_FIELD_NUMBER: _ClassVar[int]
    GAME_TIME_FIELD_NUMBER: _ClassVar[int]
    RED_HOME_HP_FIELD_NUMBER: _ClassVar[int]
    RED_TEAM_ENERGY_FIELD_NUMBER: _ClassVar[int]
    RED_TEAM_SCORE_FIELD_NUMBER: _ClassVar[int]
    blue_home_hp: int
    blue_team_energy: int
    blue_team_score: int
    game_time: int
    red_home_hp: int
    red_team_energy: int
    red_team_score: int
    def __init__(self, game_time: _Optional[int] = ..., red_team_score: _Optional[int] = ..., blue_team_score: _Optional[int] = ..., red_team_energy: _Optional[int] = ..., blue_team_energy: _Optional[int] = ..., red_home_hp: _Optional[int] = ..., blue_home_hp: _Optional[int] = ...) -> None: ...

class MessageOfBombedBullet(_message.Message):
    __slots__ = ["bomb_range", "facing_direction", "mapping_id", "type", "x", "y"]
    BOMB_RANGE_FIELD_NUMBER: _ClassVar[int]
    FACING_DIRECTION_FIELD_NUMBER: _ClassVar[int]
    MAPPING_ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    bomb_range: float
    facing_direction: float
    mapping_id: int
    type: _MessageType_pb2.BulletType
    x: int
    y: int
    def __init__(self, type: _Optional[_Union[_MessageType_pb2.BulletType, str]] = ..., x: _Optional[int] = ..., y: _Optional[int] = ..., facing_direction: _Optional[float] = ..., mapping_id: _Optional[int] = ..., bomb_range: _Optional[float] = ...) -> None: ...

class MessageOfBullet(_message.Message):
    __slots__ = ["bomb_range", "damage", "facing_direction", "guid", "speed", "team_id", "type", "x", "y"]
    BOMB_RANGE_FIELD_NUMBER: _ClassVar[int]
    DAMAGE_FIELD_NUMBER: _ClassVar[int]
    FACING_DIRECTION_FIELD_NUMBER: _ClassVar[int]
    GUID_FIELD_NUMBER: _ClassVar[int]
    SPEED_FIELD_NUMBER: _ClassVar[int]
    TEAM_ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    bomb_range: float
    damage: int
    facing_direction: float
    guid: int
    speed: int
    team_id: int
    type: _MessageType_pb2.BulletType
    x: int
    y: int
    def __init__(self, type: _Optional[_Union[_MessageType_pb2.BulletType, str]] = ..., x: _Optional[int] = ..., y: _Optional[int] = ..., facing_direction: _Optional[float] = ..., damage: _Optional[int] = ..., team_id: _Optional[int] = ..., guid: _Optional[int] = ..., bomb_range: _Optional[float] = ..., speed: _Optional[int] = ...) -> None: ...

class MessageOfCommunity(_message.Message):
    __slots__ = ["hp", "team_id", "x", "y"]
    HP_FIELD_NUMBER: _ClassVar[int]
    TEAM_ID_FIELD_NUMBER: _ClassVar[int]
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    hp: int
    team_id: int
    x: int
    y: int
    def __init__(self, x: _Optional[int] = ..., y: _Optional[int] = ..., hp: _Optional[int] = ..., team_id: _Optional[int] = ...) -> None: ...

class MessageOfFactory(_message.Message):
    __slots__ = ["hp", "team_id", "x", "y"]
    HP_FIELD_NUMBER: _ClassVar[int]
    TEAM_ID_FIELD_NUMBER: _ClassVar[int]
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    hp: int
    team_id: int
    x: int
    y: int
    def __init__(self, x: _Optional[int] = ..., y: _Optional[int] = ..., hp: _Optional[int] = ..., team_id: _Optional[int] = ...) -> None: ...

class MessageOfFort(_message.Message):
    __slots__ = ["hp", "team_id", "x", "y"]
    HP_FIELD_NUMBER: _ClassVar[int]
    TEAM_ID_FIELD_NUMBER: _ClassVar[int]
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    hp: int
    team_id: int
    x: int
    y: int
    def __init__(self, x: _Optional[int] = ..., y: _Optional[int] = ..., hp: _Optional[int] = ..., team_id: _Optional[int] = ...) -> None: ...

class MessageOfHome(_message.Message):
    __slots__ = ["hp", "team_id", "x", "y"]
    HP_FIELD_NUMBER: _ClassVar[int]
    TEAM_ID_FIELD_NUMBER: _ClassVar[int]
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    hp: int
    team_id: int
    x: int
    y: int
    def __init__(self, x: _Optional[int] = ..., y: _Optional[int] = ..., hp: _Optional[int] = ..., team_id: _Optional[int] = ...) -> None: ...

class MessageOfMap(_message.Message):
    __slots__ = ["height", "rows", "width"]
    class Row(_message.Message):
        __slots__ = ["cols"]
        COLS_FIELD_NUMBER: _ClassVar[int]
        cols: _containers.RepeatedScalarFieldContainer[_MessageType_pb2.PlaceType]
        def __init__(self, cols: _Optional[_Iterable[_Union[_MessageType_pb2.PlaceType, str]]] = ...) -> None: ...
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    ROWS_FIELD_NUMBER: _ClassVar[int]
    WIDTH_FIELD_NUMBER: _ClassVar[int]
    height: int
    rows: _containers.RepeatedCompositeFieldContainer[MessageOfMap.Row]
    width: int
    def __init__(self, height: _Optional[int] = ..., width: _Optional[int] = ..., rows: _Optional[_Iterable[_Union[MessageOfMap.Row, _Mapping]]] = ...) -> None: ...

class MessageOfNews(_message.Message):
    __slots__ = ["binary_message", "from_id", "team_id", "text_message", "to_id"]
    BINARY_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    FROM_ID_FIELD_NUMBER: _ClassVar[int]
    TEAM_ID_FIELD_NUMBER: _ClassVar[int]
    TEXT_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    TO_ID_FIELD_NUMBER: _ClassVar[int]
    binary_message: bytes
    from_id: int
    team_id: int
    text_message: str
    to_id: int
    def __init__(self, text_message: _Optional[str] = ..., binary_message: _Optional[bytes] = ..., from_id: _Optional[int] = ..., to_id: _Optional[int] = ..., team_id: _Optional[int] = ...) -> None: ...

class MessageOfObj(_message.Message):
    __slots__ = ["bombed_bullet_message", "bullet_message", "community_message", "factory_message", "fort_message", "home_message", "map_message", "news_message", "resource_message", "ship_message", "team_message", "wormhole_message"]
    BOMBED_BULLET_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    BULLET_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    COMMUNITY_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    FACTORY_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    FORT_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    HOME_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    MAP_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    NEWS_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    SHIP_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    TEAM_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    WORMHOLE_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    bombed_bullet_message: MessageOfBombedBullet
    bullet_message: MessageOfBullet
    community_message: MessageOfCommunity
    factory_message: MessageOfFactory
    fort_message: MessageOfFort
    home_message: MessageOfHome
    map_message: MessageOfMap
    news_message: MessageOfNews
    resource_message: MessageOfResource
    ship_message: MessageOfShip
    team_message: MessageOfTeam
    wormhole_message: MessageOfWormhole
    def __init__(self, ship_message: _Optional[_Union[MessageOfShip, _Mapping]] = ..., bullet_message: _Optional[_Union[MessageOfBullet, _Mapping]] = ..., factory_message: _Optional[_Union[MessageOfFactory, _Mapping]] = ..., community_message: _Optional[_Union[MessageOfCommunity, _Mapping]] = ..., fort_message: _Optional[_Union[MessageOfFort, _Mapping]] = ..., wormhole_message: _Optional[_Union[MessageOfWormhole, _Mapping]] = ..., home_message: _Optional[_Union[MessageOfHome, _Mapping]] = ..., resource_message: _Optional[_Union[MessageOfResource, _Mapping]] = ..., map_message: _Optional[_Union[MessageOfMap, _Mapping]] = ..., news_message: _Optional[_Union[MessageOfNews, _Mapping]] = ..., bombed_bullet_message: _Optional[_Union[MessageOfBombedBullet, _Mapping]] = ..., team_message: _Optional[_Union[MessageOfTeam, _Mapping]] = ...) -> None: ...

class MessageOfResource(_message.Message):
    __slots__ = ["progress", "x", "y"]
    PROGRESS_FIELD_NUMBER: _ClassVar[int]
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    progress: int
    x: int
    y: int
    def __init__(self, x: _Optional[int] = ..., y: _Optional[int] = ..., progress: _Optional[int] = ...) -> None: ...

class MessageOfShip(_message.Message):
    __slots__ = ["armor", "armor_type", "constructor_type", "facing_direction", "guid", "hp", "player_id", "producer_type", "shield", "shield_type", "ship_state", "ship_type", "speed", "team_id", "view_range", "weapon_type", "x", "y"]
    ARMOR_FIELD_NUMBER: _ClassVar[int]
    ARMOR_TYPE_FIELD_NUMBER: _ClassVar[int]
    CONSTRUCTOR_TYPE_FIELD_NUMBER: _ClassVar[int]
    FACING_DIRECTION_FIELD_NUMBER: _ClassVar[int]
    GUID_FIELD_NUMBER: _ClassVar[int]
    HP_FIELD_NUMBER: _ClassVar[int]
    PLAYER_ID_FIELD_NUMBER: _ClassVar[int]
    PRODUCER_TYPE_FIELD_NUMBER: _ClassVar[int]
    SHIELD_FIELD_NUMBER: _ClassVar[int]
    SHIELD_TYPE_FIELD_NUMBER: _ClassVar[int]
    SHIP_STATE_FIELD_NUMBER: _ClassVar[int]
    SHIP_TYPE_FIELD_NUMBER: _ClassVar[int]
    SPEED_FIELD_NUMBER: _ClassVar[int]
    TEAM_ID_FIELD_NUMBER: _ClassVar[int]
    VIEW_RANGE_FIELD_NUMBER: _ClassVar[int]
    WEAPON_TYPE_FIELD_NUMBER: _ClassVar[int]
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    armor: int
    armor_type: _MessageType_pb2.ArmorType
    constructor_type: _MessageType_pb2.ConstructorType
    facing_direction: float
    guid: int
    hp: int
    player_id: int
    producer_type: _MessageType_pb2.ProducerType
    shield: int
    shield_type: _MessageType_pb2.ShieldType
    ship_state: _MessageType_pb2.ShipState
    ship_type: _MessageType_pb2.ShipType
    speed: int
    team_id: int
    view_range: int
    weapon_type: _MessageType_pb2.WeaponType
    x: int
    y: int
    def __init__(self, x: _Optional[int] = ..., y: _Optional[int] = ..., speed: _Optional[int] = ..., hp: _Optional[int] = ..., armor: _Optional[int] = ..., shield: _Optional[int] = ..., team_id: _Optional[int] = ..., player_id: _Optional[int] = ..., guid: _Optional[int] = ..., ship_state: _Optional[_Union[_MessageType_pb2.ShipState, str]] = ..., ship_type: _Optional[_Union[_MessageType_pb2.ShipType, str]] = ..., view_range: _Optional[int] = ..., producer_type: _Optional[_Union[_MessageType_pb2.ProducerType, str]] = ..., constructor_type: _Optional[_Union[_MessageType_pb2.ConstructorType, str]] = ..., armor_type: _Optional[_Union[_MessageType_pb2.ArmorType, str]] = ..., shield_type: _Optional[_Union[_MessageType_pb2.ShieldType, str]] = ..., weapon_type: _Optional[_Union[_MessageType_pb2.WeaponType, str]] = ..., facing_direction: _Optional[float] = ...) -> None: ...

class MessageOfTeam(_message.Message):
    __slots__ = ["energy", "player_id", "score", "team_id"]
    ENERGY_FIELD_NUMBER: _ClassVar[int]
    PLAYER_ID_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    TEAM_ID_FIELD_NUMBER: _ClassVar[int]
    energy: int
    player_id: int
    score: int
    team_id: int
    def __init__(self, team_id: _Optional[int] = ..., player_id: _Optional[int] = ..., score: _Optional[int] = ..., energy: _Optional[int] = ...) -> None: ...

class MessageOfWormhole(_message.Message):
    __slots__ = ["hp", "id", "x", "y"]
    HP_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    hp: int
    id: int
    x: int
    y: int
    def __init__(self, x: _Optional[int] = ..., y: _Optional[int] = ..., hp: _Optional[int] = ..., id: _Optional[int] = ...) -> None: ...

class MessageToClient(_message.Message):
    __slots__ = ["all_message", "game_state", "obj_message"]
    ALL_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    GAME_STATE_FIELD_NUMBER: _ClassVar[int]
    OBJ_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    all_message: MessageOfAll
    game_state: _MessageType_pb2.GameState
    obj_message: _containers.RepeatedCompositeFieldContainer[MessageOfObj]
    def __init__(self, obj_message: _Optional[_Iterable[_Union[MessageOfObj, _Mapping]]] = ..., game_state: _Optional[_Union[_MessageType_pb2.GameState, str]] = ..., all_message: _Optional[_Union[MessageOfAll, _Mapping]] = ...) -> None: ...

class MoveRes(_message.Message):
    __slots__ = ["act_success", "actual_angle", "actual_speed"]
    ACTUAL_ANGLE_FIELD_NUMBER: _ClassVar[int]
    ACTUAL_SPEED_FIELD_NUMBER: _ClassVar[int]
    ACT_SUCCESS_FIELD_NUMBER: _ClassVar[int]
    act_success: bool
    actual_angle: float
    actual_speed: int
    def __init__(self, actual_speed: _Optional[int] = ..., actual_angle: _Optional[float] = ..., act_success: bool = ...) -> None: ...

class ShipInfoRes(_message.Message):
    __slots__ = ["ship_info"]
    SHIP_INFO_FIELD_NUMBER: _ClassVar[int]
    ship_info: _containers.RepeatedCompositeFieldContainer[MessageOfShip]
    def __init__(self, ship_info: _Optional[_Iterable[_Union[MessageOfShip, _Mapping]]] = ...) -> None: ...
