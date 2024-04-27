# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Message2Clients.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import MessageType_pb2 as MessageType__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15Message2Clients.proto\x12\x08protobuf\x1a\x11MessageType.proto\"\xf2\x03\n\rMessageOfShip\x12\t\n\x01x\x18\x01 \x01(\x05\x12\t\n\x01y\x18\x02 \x01(\x05\x12\r\n\x05speed\x18\x03 \x01(\x05\x12\n\n\x02hp\x18\x04 \x01(\x05\x12\r\n\x05\x61rmor\x18\x05 \x01(\x05\x12\x0e\n\x06shield\x18\x06 \x01(\x05\x12\x0f\n\x07team_id\x18\x07 \x01(\x03\x12\x11\n\tplayer_id\x18\x08 \x01(\x03\x12\x0c\n\x04guid\x18\t \x01(\x03\x12\'\n\nship_state\x18\n \x01(\x0e\x32\x13.protobuf.ShipState\x12%\n\tship_type\x18\x0b \x01(\x0e\x32\x12.protobuf.ShipType\x12\x12\n\nview_range\x18\x0c \x01(\x05\x12-\n\rproducer_type\x18\r \x01(\x0e\x32\x16.protobuf.ProducerType\x12\x33\n\x10\x63onstructor_type\x18\x0e \x01(\x0e\x32\x19.protobuf.ConstructorType\x12\'\n\narmor_type\x18\x0f \x01(\x0e\x32\x13.protobuf.ArmorType\x12)\n\x0bshield_type\x18\x10 \x01(\x0e\x32\x14.protobuf.ShieldType\x12)\n\x0bweapon_type\x18\x11 \x01(\x0e\x32\x14.protobuf.WeaponType\x12\x18\n\x10\x66\x61\x63ing_direction\x18\x12 \x01(\x01\"\xb7\x01\n\x0fMessageOfBullet\x12\"\n\x04type\x18\x01 \x01(\x0e\x32\x14.protobuf.BulletType\x12\t\n\x01x\x18\x02 \x01(\x05\x12\t\n\x01y\x18\x03 \x01(\x05\x12\x18\n\x10\x66\x61\x63ing_direction\x18\x04 \x01(\x01\x12\x0e\n\x06\x64\x61mage\x18\x05 \x01(\x05\x12\x0f\n\x07team_id\x18\x06 \x01(\x03\x12\x0c\n\x04guid\x18\x07 \x01(\x03\x12\x12\n\nbomb_range\x18\x08 \x01(\x01\x12\r\n\x05speed\x18\t \x01(\x05\"\x93\x01\n\x15MessageOfBombedBullet\x12\"\n\x04type\x18\x01 \x01(\x0e\x32\x14.protobuf.BulletType\x12\t\n\x01x\x18\x02 \x01(\x05\x12\t\n\x01y\x18\x03 \x01(\x05\x12\x18\n\x10\x66\x61\x63ing_direction\x18\x04 \x01(\x01\x12\x12\n\nmapping_id\x18\x05 \x01(\x03\x12\x12\n\nbomb_range\x18\x06 \x01(\x01\"E\n\x10MessageOfFactory\x12\t\n\x01x\x18\x01 \x01(\x05\x12\t\n\x01y\x18\x02 \x01(\x05\x12\n\n\x02hp\x18\x03 \x01(\x05\x12\x0f\n\x07team_id\x18\x04 \x01(\x03\"G\n\x12MessageOfCommunity\x12\t\n\x01x\x18\x01 \x01(\x05\x12\t\n\x01y\x18\x02 \x01(\x05\x12\n\n\x02hp\x18\x03 \x01(\x05\x12\x0f\n\x07team_id\x18\x04 \x01(\x03\"B\n\rMessageOfFort\x12\t\n\x01x\x18\x01 \x01(\x05\x12\t\n\x01y\x18\x02 \x01(\x05\x12\n\n\x02hp\x18\x03 \x01(\x05\x12\x0f\n\x07team_id\x18\x04 \x01(\x03\"A\n\x11MessageOfWormhole\x12\t\n\x01x\x18\x01 \x01(\x05\x12\t\n\x01y\x18\x02 \x01(\x05\x12\n\n\x02hp\x18\x03 \x01(\x05\x12\n\n\x02id\x18\x04 \x01(\x05\";\n\x11MessageOfResource\x12\t\n\x01x\x18\x01 \x01(\x05\x12\t\n\x01y\x18\x02 \x01(\x05\x12\x10\n\x08progress\x18\x03 \x01(\x05\"B\n\rMessageOfHome\x12\t\n\x01x\x18\x01 \x01(\x05\x12\t\n\x01y\x18\x02 \x01(\x05\x12\n\n\x02hp\x18\x03 \x01(\x05\x12\x0f\n\x07team_id\x18\x04 \x01(\x03\"\x81\x01\n\x0cMessageOfMap\x12\x0e\n\x06height\x18\x01 \x01(\r\x12\r\n\x05width\x18\x02 \x01(\r\x12(\n\x04rows\x18\x03 \x03(\x0b\x32\x1a.protobuf.MessageOfMap.Row\x1a(\n\x03Row\x12!\n\x04\x63ols\x18\x01 \x03(\x0e\x32\x13.protobuf.PlaceType\"R\n\rMessageOfTeam\x12\x0f\n\x07team_id\x18\x01 \x01(\x03\x12\x11\n\tplayer_id\x18\x02 \x01(\x03\x12\r\n\x05score\x18\x03 \x01(\x03\x12\x0e\n\x06\x65nergy\x18\x04 \x01(\x03\"\x9f\x05\n\x0cMessageOfObj\x12/\n\x0cship_message\x18\x01 \x01(\x0b\x32\x17.protobuf.MessageOfShipH\x00\x12\x33\n\x0e\x62ullet_message\x18\x02 \x01(\x0b\x32\x19.protobuf.MessageOfBulletH\x00\x12\x35\n\x0f\x66\x61\x63tory_message\x18\x03 \x01(\x0b\x32\x1a.protobuf.MessageOfFactoryH\x00\x12\x39\n\x11\x63ommunity_message\x18\x04 \x01(\x0b\x32\x1c.protobuf.MessageOfCommunityH\x00\x12/\n\x0c\x66ort_message\x18\x05 \x01(\x0b\x32\x17.protobuf.MessageOfFortH\x00\x12\x37\n\x10wormhole_message\x18\x06 \x01(\x0b\x32\x1b.protobuf.MessageOfWormholeH\x00\x12/\n\x0chome_message\x18\x07 \x01(\x0b\x32\x17.protobuf.MessageOfHomeH\x00\x12\x37\n\x10resource_message\x18\x08 \x01(\x0b\x32\x1b.protobuf.MessageOfResourceH\x00\x12-\n\x0bmap_message\x18\t \x01(\x0b\x32\x16.protobuf.MessageOfMapH\x00\x12/\n\x0cnews_message\x18\n \x01(\x0b\x32\x17.protobuf.MessageOfNewsH\x00\x12@\n\x15\x62ombed_bullet_message\x18\x0b \x01(\x0b\x32\x1f.protobuf.MessageOfBombedBulletH\x00\x12/\n\x0cteam_message\x18\x0c \x01(\x0b\x32\x17.protobuf.MessageOfTeamH\x00\x42\x10\n\x0emessage_of_obj\"\xb0\x01\n\x0cMessageOfAll\x12\x11\n\tgame_time\x18\x01 \x01(\x05\x12\x16\n\x0ered_team_score\x18\x02 \x01(\x05\x12\x17\n\x0f\x62lue_team_score\x18\x03 \x01(\x05\x12\x17\n\x0fred_team_energy\x18\x04 \x01(\x05\x12\x18\n\x10\x62lue_team_energy\x18\x05 \x01(\x05\x12\x13\n\x0bred_home_hp\x18\x06 \x01(\x05\x12\x14\n\x0c\x62lue_home_hp\x18\x07 \x01(\x05\"\x94\x01\n\x0fMessageToClient\x12+\n\x0bobj_message\x18\x01 \x03(\x0b\x32\x16.protobuf.MessageOfObj\x12\'\n\ngame_state\x18\x02 \x01(\x0e\x32\x13.protobuf.GameState\x12+\n\x0b\x61ll_message\x18\x03 \x01(\x0b\x32\x16.protobuf.MessageOfAll\"J\n\x07MoveRes\x12\x14\n\x0c\x61\x63tual_speed\x18\x01 \x01(\x03\x12\x14\n\x0c\x61\x63tual_angle\x18\x02 \x01(\x01\x12\x13\n\x0b\x61\x63t_success\x18\x03 \x01(\x08\"6\n\x0c\x42uildShipRes\x12\x13\n\x0b\x61\x63t_success\x18\x01 \x01(\x08\x12\x11\n\tplayer_id\x18\x02 \x01(\x03\"\x1e\n\x07\x42oolRes\x12\x13\n\x0b\x61\x63t_success\x18\x01 \x01(\x08\"9\n\x0bShipInfoRes\x12*\n\tship_info\x18\x01 \x03(\x0b\x32\x17.protobuf.MessageOfShip\"\x19\n\x06\x45\x63oRes\x12\x0f\n\x07\x65\x63onomy\x18\x01 \x01(\x03\"z\n\rMessageOfNews\x12\x16\n\x0ctext_message\x18\x01 \x01(\tH\x00\x12\x18\n\x0e\x62inary_message\x18\x02 \x01(\x0cH\x00\x12\x0f\n\x07\x66rom_id\x18\x03 \x01(\x03\x12\r\n\x05to_id\x18\x04 \x01(\x03\x12\x0f\n\x07team_id\x18\x05 \x01(\x03\x42\x06\n\x04newsb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'Message2Clients_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _MESSAGEOFSHIP._serialized_start=55
  _MESSAGEOFSHIP._serialized_end=553
  _MESSAGEOFBULLET._serialized_start=556
  _MESSAGEOFBULLET._serialized_end=739
  _MESSAGEOFBOMBEDBULLET._serialized_start=742
  _MESSAGEOFBOMBEDBULLET._serialized_end=889
  _MESSAGEOFFACTORY._serialized_start=891
  _MESSAGEOFFACTORY._serialized_end=960
  _MESSAGEOFCOMMUNITY._serialized_start=962
  _MESSAGEOFCOMMUNITY._serialized_end=1033
  _MESSAGEOFFORT._serialized_start=1035
  _MESSAGEOFFORT._serialized_end=1101
  _MESSAGEOFWORMHOLE._serialized_start=1103
  _MESSAGEOFWORMHOLE._serialized_end=1168
  _MESSAGEOFRESOURCE._serialized_start=1170
  _MESSAGEOFRESOURCE._serialized_end=1229
  _MESSAGEOFHOME._serialized_start=1231
  _MESSAGEOFHOME._serialized_end=1297
  _MESSAGEOFMAP._serialized_start=1300
  _MESSAGEOFMAP._serialized_end=1429
  _MESSAGEOFMAP_ROW._serialized_start=1389
  _MESSAGEOFMAP_ROW._serialized_end=1429
  _MESSAGEOFTEAM._serialized_start=1431
  _MESSAGEOFTEAM._serialized_end=1513
  _MESSAGEOFOBJ._serialized_start=1516
  _MESSAGEOFOBJ._serialized_end=2187
  _MESSAGEOFALL._serialized_start=2190
  _MESSAGEOFALL._serialized_end=2366
  _MESSAGETOCLIENT._serialized_start=2369
  _MESSAGETOCLIENT._serialized_end=2517
  _MOVERES._serialized_start=2519
  _MOVERES._serialized_end=2593
  _BUILDSHIPRES._serialized_start=2595
  _BUILDSHIPRES._serialized_end=2649
  _BOOLRES._serialized_start=2651
  _BOOLRES._serialized_end=2681
  _SHIPINFORES._serialized_start=2683
  _SHIPINFORES._serialized_end=2740
  _ECORES._serialized_start=2742
  _ECORES._serialized_end=2767
  _MESSAGEOFNEWS._serialized_start=2769
  _MESSAGEOFNEWS._serialized_end=2891
# @@protoc_insertion_point(module_scope)