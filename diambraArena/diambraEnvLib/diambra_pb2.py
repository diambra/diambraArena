# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: diambra.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rdiambra.proto\x12\x07\x64iambra\"\x07\n\x05\x45mpty\"\x1f\n\x0b\x45nvSettings\x12\x10\n\x08settings\x18\x01 \x01(\t\"9\n\x11\x45nvInfoAndIntData\x12\x0f\n\x07\x65nvInfo\x18\x01 \x01(\t\x12\x13\n\x0bintDataList\x18\x02 \x01(\t\"E\n\x07\x43ommand\x12\r\n\x05P1mov\x18\x01 \x01(\x05\x12\r\n\x05P1att\x18\x02 \x01(\x05\x12\r\n\x05P2mov\x18\x03 \x01(\x05\x12\r\n\x05P2att\x18\x04 \x01(\x05\")\n\x03Obs\x12\x13\n\x0bobservation\x18\x01 \x01(\t\x12\r\n\x05\x66rame\x18\x02 \x01(\x0c\x32\xf6\x01\n\tEnvServer\x12=\n\x07\x45nvInit\x12\x14.diambra.EnvSettings\x1a\x1a.diambra.EnvInfoAndIntData\"\x00\x12\'\n\x05Reset\x12\x0e.diambra.Empty\x1a\x0c.diambra.Obs\"\x00\x12*\n\x06Step1P\x12\x10.diambra.Command\x1a\x0c.diambra.Obs\"\x00\x12*\n\x06Step2P\x12\x10.diambra.Command\x1a\x0c.diambra.Obs\"\x00\x12)\n\x05\x43lose\x12\x0e.diambra.Empty\x1a\x0e.diambra.Empty\"\x00\x42\x06\xa2\x02\x03HLWb\x06proto3')



_EMPTY = DESCRIPTOR.message_types_by_name['Empty']
_ENVSETTINGS = DESCRIPTOR.message_types_by_name['EnvSettings']
_ENVINFOANDINTDATA = DESCRIPTOR.message_types_by_name['EnvInfoAndIntData']
_COMMAND = DESCRIPTOR.message_types_by_name['Command']
_OBS = DESCRIPTOR.message_types_by_name['Obs']
Empty = _reflection.GeneratedProtocolMessageType('Empty', (_message.Message,), {
  'DESCRIPTOR' : _EMPTY,
  '__module__' : 'diambra_pb2'
  # @@protoc_insertion_point(class_scope:diambra.Empty)
  })
_sym_db.RegisterMessage(Empty)

EnvSettings = _reflection.GeneratedProtocolMessageType('EnvSettings', (_message.Message,), {
  'DESCRIPTOR' : _ENVSETTINGS,
  '__module__' : 'diambra_pb2'
  # @@protoc_insertion_point(class_scope:diambra.EnvSettings)
  })
_sym_db.RegisterMessage(EnvSettings)

EnvInfoAndIntData = _reflection.GeneratedProtocolMessageType('EnvInfoAndIntData', (_message.Message,), {
  'DESCRIPTOR' : _ENVINFOANDINTDATA,
  '__module__' : 'diambra_pb2'
  # @@protoc_insertion_point(class_scope:diambra.EnvInfoAndIntData)
  })
_sym_db.RegisterMessage(EnvInfoAndIntData)

Command = _reflection.GeneratedProtocolMessageType('Command', (_message.Message,), {
  'DESCRIPTOR' : _COMMAND,
  '__module__' : 'diambra_pb2'
  # @@protoc_insertion_point(class_scope:diambra.Command)
  })
_sym_db.RegisterMessage(Command)

Obs = _reflection.GeneratedProtocolMessageType('Obs', (_message.Message,), {
  'DESCRIPTOR' : _OBS,
  '__module__' : 'diambra_pb2'
  # @@protoc_insertion_point(class_scope:diambra.Obs)
  })
_sym_db.RegisterMessage(Obs)

_ENVSERVER = DESCRIPTOR.services_by_name['EnvServer']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\242\002\003HLW'
  _EMPTY._serialized_start=26
  _EMPTY._serialized_end=33
  _ENVSETTINGS._serialized_start=35
  _ENVSETTINGS._serialized_end=66
  _ENVINFOANDINTDATA._serialized_start=68
  _ENVINFOANDINTDATA._serialized_end=125
  _COMMAND._serialized_start=127
  _COMMAND._serialized_end=196
  _OBS._serialized_start=198
  _OBS._serialized_end=239
  _ENVSERVER._serialized_start=242
  _ENVSERVER._serialized_end=488
# @@protoc_insertion_point(module_scope)