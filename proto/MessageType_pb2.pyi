from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

ARC: BulletType
ARCGUN: WeaponType
ARMOR1: ArmorType
ARMOR2: ArmorType
ARMOR3: ArmorType
ASTEROID: PlaceType
ATTACKING: ShipState
BINARY: NewsType
BLUE: PlayerTeam
CIRCLE: ShapeType
CIVILIAN_SHIP: ShipType
COMMUNITY: ConstructionType
CONSTRUCTING: ShipState
CONSTRUCTION: PlaceType
CONSTRUCTOR1: ConstructorType
CONSTRUCTOR2: ConstructorType
CONSTRUCTOR3: ConstructorType
DESCRIPTOR: _descriptor.FileDescriptor
FACTORY: ConstructionType
FLAG_SHIP: ShipType
FORT: ConstructionType
GAME_END: GameState
GAME_RUNNING: GameState
GAME_START: GameState
HOME: PlaceType
IDLE: ShipState
LASER: BulletType
LASERGUN: WeaponType
MILITARY_SHIP: ShipType
MISSILE: BulletType
MISSILEGUN: WeaponType
MODULE_ARCGUN: ModuleType
MODULE_ARMOR1: ModuleType
MODULE_ARMOR2: ModuleType
MODULE_ARMOR3: ModuleType
MODULE_CONSTRUCTOR1: ModuleType
MODULE_CONSTRUCTOR2: ModuleType
MODULE_CONSTRUCTOR3: ModuleType
MODULE_LASERGUN: ModuleType
MODULE_MISSILEGUN: ModuleType
MODULE_PLASMAGUN: ModuleType
MODULE_PRODUCER1: ModuleType
MODULE_PRODUCER2: ModuleType
MODULE_PRODUCER3: ModuleType
MODULE_SHELLGUN: ModuleType
MODULE_SHIELD1: ModuleType
MODULE_SHIELD2: ModuleType
MODULE_SHIELD3: ModuleType
MOVING: ShipState
NULL_ARMOR_TYPE: ArmorType
NULL_BULLET_TYPE: BulletType
NULL_CONSTRUCTION_TYPE: ConstructionType
NULL_CONSTRUCTOR_TYPE: ConstructorType
NULL_GAME_STATE: GameState
NULL_MODULE_TYPE: ModuleType
NULL_NEWS_TYPE: NewsType
NULL_PLACE_TYPE: PlaceType
NULL_PLAYER_TYPE: PlayerType
NULL_PRODUCER_TYPE: ProducerType
NULL_SHAPE_TYPE: ShapeType
NULL_SHIELD_TYPE: ShieldType
NULL_SHIP_TYPE: ShipType
NULL_STATUS: ShipState
NULL_TEAM: PlayerTeam
NULL_WEAPON_TYPE: WeaponType
PLASMA: BulletType
PLASMAGUN: WeaponType
PRODUCER1: ProducerType
PRODUCER2: ProducerType
PRODUCER3: ProducerType
PRODUCING: ShipState
RECOVERING: ShipState
RECYCLING: ShipState
RED: PlayerTeam
RESOURCE: PlaceType
RUIN: PlaceType
SHADOW: PlaceType
SHELL: BulletType
SHELLGUN: WeaponType
SHIELD1: ShieldType
SHIELD2: ShieldType
SHIELD3: ShieldType
SHIP: PlayerType
SPACE: PlaceType
SQUARE: ShapeType
STUNNED: ShipState
SWINGING: ShipState
TEAM: PlayerType
TEXT: NewsType
WORMHOLE: PlaceType

class GameState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class PlaceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class ShapeType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class PlayerType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class ShipType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class ShipState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class WeaponType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class ConstructorType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class ArmorType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class ShieldType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class ProducerType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class ModuleType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class BulletType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class ConstructionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class NewsType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class PlayerTeam(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
