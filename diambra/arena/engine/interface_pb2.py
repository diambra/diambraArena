# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: diambra/arena/engine/interface.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$diambra/arena/engine/interface.proto\x12\tinterface\"\x07\n\x05\x45mpty\"!\n\x07Outfits\x12\n\n\x02p1\x18\x01 \x01(\x05\x12\n\n\x02p2\x18\x02 \x01(\x05\"2\n\x16\x43umulativeRewardBounds\x12\x0b\n\x03min\x18\x01 \x01(\x05\x12\x0b\n\x03max\x18\x02 \x01(\x05\"V\n\x0c\x41\x63tionSpaces\x12\"\n\x02p1\x18\x01 \x01(\x0e\x32\x16.interface.ActionSpace\x12\"\n\x02p2\x18\x02 \x01(\x0e\x32\x16.interface.ActionSpace\"3\n\x19\x41ttackButtonsCombinations\x12\n\n\x02p1\x18\x01 \x01(\x08\x12\n\n\x02p2\x18\x02 \x01(\x08\"-\n\nFrameShape\x12\t\n\x01h\x18\x01 \x01(\x05\x12\t\n\x01w\x18\x02 \x01(\x05\x12\t\n\x01\x63\x18\x03 \x01(\x05\"?\n\x08RamState\x12\x0c\n\x04type\x18\x01 \x01(\x05\x12\x0b\n\x03min\x18\x02 \x01(\x05\x12\x0b\n\x03max\x18\x03 \x01(\x05\x12\x0b\n\x03val\x18\x04 \x01(\x05\"%\n\x0c\x45rrorMessage\x12\x15\n\rerror_message\x18\x01 \x01(\t\"\xd8\x07\n\x0b\x45nvSettings\x12\x0f\n\x07game_id\x18\x01 \x01(\t\x12\x15\n\rcontinue_game\x18\x02 \x01(\x01\x12\x12\n\nshow_final\x18\x03 \x01(\x08\x12\x12\n\nstep_ratio\x18\x04 \x01(\x05\x12\x0e\n\x06player\x18\x05 \x01(\t\x12\x12\n\ndifficulty\x18\x06 \x01(\x05\x12\x35\n\ncharacters\x18\x07 \x01(\x0b\x32!.interface.EnvSettings.Characters\x12#\n\x07outfits\x18\x08 \x01(\x0b\x32\x12.interface.Outfits\x12*\n\x0b\x66rame_shape\x18\t \x01(\x0b\x32\x15.interface.FrameShape\x12.\n\raction_spaces\x18\n \x01(\x0b\x32\x17.interface.ActionSpaces\x12I\n\x1b\x61ttack_buttons_combinations\x18\x0b \x01(\x0b\x32$.interface.AttackButtonsCombinations\x12\x10\n\x08hardcore\x18\x0c \x01(\x08\x12\x18\n\x10\x64isable_keyboard\x18\r \x01(\x08\x12\x18\n\x10\x64isable_joystick\x18\x0e \x01(\x08\x12\x0c\n\x04rank\x18\x0f \x01(\x05\x12\x13\n\x0brandom_seed\x18\x10 \x01(\x05\x12\x34\n\nsuper_arts\x18\x11 \x01(\x0b\x32 .interface.EnvSettings.SuperArts\x12\r\n\x05tower\x18\x12 \x01(\x05\x12>\n\x0f\x66ighting_styles\x18\x13 \x01(\x0b\x32%.interface.EnvSettings.FightingStyles\x12>\n\x0fultimate_styles\x18\x14 \x01(\x0b\x32%.interface.EnvSettings.UltimateStyles\x1a$\n\nCharacters\x12\n\n\x02p1\x18\x01 \x03(\t\x12\n\n\x02p2\x18\x02 \x03(\t\x1a#\n\tSuperArts\x12\n\n\x02p1\x18\x01 \x01(\x05\x12\n\n\x02p2\x18\x02 \x01(\x05\x1a(\n\x0e\x46ightingStyles\x12\n\n\x02p1\x18\x01 \x01(\x05\x12\n\n\x02p2\x18\x02 \x01(\x05\x1a\x39\n\rUltimateStyle\x12\x0c\n\x04\x64\x61sh\x18\x01 \x01(\x05\x12\r\n\x05\x65vade\x18\x02 \x01(\x05\x12\x0b\n\x03\x62\x61r\x18\x03 \x01(\x05\x1at\n\x0eUltimateStyles\x12\x30\n\x02p1\x18\x01 \x01(\x0b\x32$.interface.EnvSettings.UltimateStyle\x12\x30\n\x02p2\x18\x02 \x01(\x0b\x32$.interface.EnvSettings.UltimateStyle\"\xd5\x06\n\x0f\x45nvInitResponse\x12\x46\n\x11\x61vailable_actions\x18\x01 \x01(\x0b\x32+.interface.EnvInitResponse.AvailableActions\x12*\n\x0b\x66rame_shape\x18\x02 \x01(\x0b\x32\x15.interface.FrameShape\x12\x14\n\x0c\x64\x65lta_health\x18\x03 \x01(\x05\x12\x11\n\tmax_stage\x18\x04 \x01(\x05\x12\x43\n\x18\x63umulative_reward_bounds\x18\x05 \x01(\x0b\x32!.interface.CumulativeRewardBounds\x12\x11\n\tchar_list\x18\x06 \x03(\t\x12\x33\n\x07\x62uttons\x18\x07 \x01(\x0b\x32\".interface.EnvInitResponse.Buttons\x12@\n\x0e\x62utton_mapping\x18\x08 \x01(\x0b\x32(.interface.EnvInitResponse.ButtonMapping\x12=\n\nram_states\x18\t \x03(\x0b\x32).interface.EnvInitResponse.RamStatesEntry\x1a\x36\n\x14MoveAndAttackActions\x12\r\n\x05moves\x18\x01 \x01(\x05\x12\x0f\n\x07\x61ttacks\x18\x02 \x01(\x05\x1a\xbb\x01\n\x10\x41vailableActions\x12Q\n\x18with_buttons_combination\x18\x01 \x01(\x0b\x32/.interface.EnvInitResponse.MoveAndAttackActions\x12T\n\x1bwithout_buttons_combination\x18\x02 \x01(\x0b\x32/.interface.EnvInitResponse.MoveAndAttackActions\x1a)\n\x07\x42uttons\x12\r\n\x05moves\x18\x01 \x03(\t\x12\x0f\n\x07\x61ttacks\x18\x02 \x03(\t\x1a/\n\rButtonMapping\x12\r\n\x05moves\x18\x01 \x03(\t\x12\x0f\n\x07\x61ttacks\x18\x02 \x03(\t\x1a\x45\n\x0eRamStatesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\"\n\x05value\x18\x02 \x01(\x0b\x32\x13.interface.RamState:\x02\x38\x01\"&\n\x06\x41\x63tion\x12\x0c\n\x04move\x18\x01 \x01(\x05\x12\x0e\n\x06\x61ttack\x18\x02 \x01(\x05\"G\n\x07\x41\x63tions\x12\x1d\n\x02p1\x18\x01 \x01(\x0b\x32\x11.interface.Action\x12\x1d\n\x02p2\x18\x02 \x01(\x0b\x32\x11.interface.Action\"\xf7\x02\n\x0bObservation\x12#\n\x07\x61\x63tions\x18\x01 \x01(\x0b\x32\x12.interface.Actions\x12\x39\n\nram_states\x18\x02 \x03(\x0b\x32%.interface.Observation.RamStatesEntry\x12\x34\n\ngame_state\x18\x03 \x01(\x0b\x32 .interface.Observation.GameState\x12\x0e\n\x06player\x18\x04 \x01(\t\x12\r\n\x05\x66rame\x18\x05 \x01(\x0c\x12\x0e\n\x06reward\x18\x06 \x01(\x05\x1a\\\n\tGameState\x12\x12\n\nround_done\x18\x01 \x01(\x08\x12\x12\n\nstage_done\x18\x02 \x01(\x08\x12\x11\n\tgame_done\x18\x03 \x01(\x08\x12\x14\n\x0c\x65pisode_done\x18\x04 \x01(\x08\x1a\x45\n\x0eRamStatesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\"\n\x05value\x18\x02 \x01(\x0b\x32\x13.interface.RamState:\x02\x38\x01*I\n\x0b\x41\x63tionSpace\x12\x19\n\x15\x41\x43TION_SPACE_DISCRETE\x10\x00\x12\x1f\n\x1b\x41\x43TION_SPACE_MULTI_DISCRETE\x10\x01\x32\x8b\x03\n\tEnvServer\x12\x37\n\x08GetError\x12\x10.interface.Empty\x1a\x17.interface.ErrorMessage\"\x00\x12?\n\x07\x45nvInit\x12\x16.interface.EnvSettings\x1a\x1a.interface.EnvInitResponse\"\x00\x12\x33\n\x05Reset\x12\x10.interface.Empty\x1a\x16.interface.Observation\"\x00\x12\x36\n\x06Step1P\x12\x12.interface.Actions\x1a\x16.interface.Observation\"\x00\x12\x36\n\x06Step2P\x12\x12.interface.Actions\x1a\x16.interface.Observation\"\x00\x12-\n\x05\x43lose\x12\x10.interface.Empty\x1a\x10.interface.Empty\"\x00\x12\x30\n\x08Shutdown\x12\x10.interface.Empty\x1a\x10.interface.Empty\"\x00\x42\x06\xa2\x02\x03HLWb\x06proto3')

_ACTIONSPACE = DESCRIPTOR.enum_types_by_name['ActionSpace']
ActionSpace = enum_type_wrapper.EnumTypeWrapper(_ACTIONSPACE)
ACTION_SPACE_DISCRETE = 0
ACTION_SPACE_MULTI_DISCRETE = 1


_EMPTY = DESCRIPTOR.message_types_by_name['Empty']
_OUTFITS = DESCRIPTOR.message_types_by_name['Outfits']
_CUMULATIVEREWARDBOUNDS = DESCRIPTOR.message_types_by_name['CumulativeRewardBounds']
_ACTIONSPACES = DESCRIPTOR.message_types_by_name['ActionSpaces']
_ATTACKBUTTONSCOMBINATIONS = DESCRIPTOR.message_types_by_name['AttackButtonsCombinations']
_FRAMESHAPE = DESCRIPTOR.message_types_by_name['FrameShape']
_RAMSTATE = DESCRIPTOR.message_types_by_name['RamState']
_ERRORMESSAGE = DESCRIPTOR.message_types_by_name['ErrorMessage']
_ENVSETTINGS = DESCRIPTOR.message_types_by_name['EnvSettings']
_ENVSETTINGS_CHARACTERS = _ENVSETTINGS.nested_types_by_name['Characters']
_ENVSETTINGS_SUPERARTS = _ENVSETTINGS.nested_types_by_name['SuperArts']
_ENVSETTINGS_FIGHTINGSTYLES = _ENVSETTINGS.nested_types_by_name['FightingStyles']
_ENVSETTINGS_ULTIMATESTYLE = _ENVSETTINGS.nested_types_by_name['UltimateStyle']
_ENVSETTINGS_ULTIMATESTYLES = _ENVSETTINGS.nested_types_by_name['UltimateStyles']
_ENVINITRESPONSE = DESCRIPTOR.message_types_by_name['EnvInitResponse']
_ENVINITRESPONSE_MOVEANDATTACKACTIONS = _ENVINITRESPONSE.nested_types_by_name['MoveAndAttackActions']
_ENVINITRESPONSE_AVAILABLEACTIONS = _ENVINITRESPONSE.nested_types_by_name['AvailableActions']
_ENVINITRESPONSE_BUTTONS = _ENVINITRESPONSE.nested_types_by_name['Buttons']
_ENVINITRESPONSE_BUTTONMAPPING = _ENVINITRESPONSE.nested_types_by_name['ButtonMapping']
_ENVINITRESPONSE_RAMSTATESENTRY = _ENVINITRESPONSE.nested_types_by_name['RamStatesEntry']
_ACTION = DESCRIPTOR.message_types_by_name['Action']
_ACTIONS = DESCRIPTOR.message_types_by_name['Actions']
_OBSERVATION = DESCRIPTOR.message_types_by_name['Observation']
_OBSERVATION_GAMESTATE = _OBSERVATION.nested_types_by_name['GameState']
_OBSERVATION_RAMSTATESENTRY = _OBSERVATION.nested_types_by_name['RamStatesEntry']
Empty = _reflection.GeneratedProtocolMessageType('Empty', (_message.Message,), {
  'DESCRIPTOR' : _EMPTY,
  '__module__' : 'diambra.arena.engine.interface_pb2'
  # @@protoc_insertion_point(class_scope:interface.Empty)
  })
_sym_db.RegisterMessage(Empty)

Outfits = _reflection.GeneratedProtocolMessageType('Outfits', (_message.Message,), {
  'DESCRIPTOR' : _OUTFITS,
  '__module__' : 'diambra.arena.engine.interface_pb2'
  # @@protoc_insertion_point(class_scope:interface.Outfits)
  })
_sym_db.RegisterMessage(Outfits)

CumulativeRewardBounds = _reflection.GeneratedProtocolMessageType('CumulativeRewardBounds', (_message.Message,), {
  'DESCRIPTOR' : _CUMULATIVEREWARDBOUNDS,
  '__module__' : 'diambra.arena.engine.interface_pb2'
  # @@protoc_insertion_point(class_scope:interface.CumulativeRewardBounds)
  })
_sym_db.RegisterMessage(CumulativeRewardBounds)

ActionSpaces = _reflection.GeneratedProtocolMessageType('ActionSpaces', (_message.Message,), {
  'DESCRIPTOR' : _ACTIONSPACES,
  '__module__' : 'diambra.arena.engine.interface_pb2'
  # @@protoc_insertion_point(class_scope:interface.ActionSpaces)
  })
_sym_db.RegisterMessage(ActionSpaces)

AttackButtonsCombinations = _reflection.GeneratedProtocolMessageType('AttackButtonsCombinations', (_message.Message,), {
  'DESCRIPTOR' : _ATTACKBUTTONSCOMBINATIONS,
  '__module__' : 'diambra.arena.engine.interface_pb2'
  # @@protoc_insertion_point(class_scope:interface.AttackButtonsCombinations)
  })
_sym_db.RegisterMessage(AttackButtonsCombinations)

FrameShape = _reflection.GeneratedProtocolMessageType('FrameShape', (_message.Message,), {
  'DESCRIPTOR' : _FRAMESHAPE,
  '__module__' : 'diambra.arena.engine.interface_pb2'
  # @@protoc_insertion_point(class_scope:interface.FrameShape)
  })
_sym_db.RegisterMessage(FrameShape)

RamState = _reflection.GeneratedProtocolMessageType('RamState', (_message.Message,), {
  'DESCRIPTOR' : _RAMSTATE,
  '__module__' : 'diambra.arena.engine.interface_pb2'
  # @@protoc_insertion_point(class_scope:interface.RamState)
  })
_sym_db.RegisterMessage(RamState)

ErrorMessage = _reflection.GeneratedProtocolMessageType('ErrorMessage', (_message.Message,), {
  'DESCRIPTOR' : _ERRORMESSAGE,
  '__module__' : 'diambra.arena.engine.interface_pb2'
  # @@protoc_insertion_point(class_scope:interface.ErrorMessage)
  })
_sym_db.RegisterMessage(ErrorMessage)

EnvSettings = _reflection.GeneratedProtocolMessageType('EnvSettings', (_message.Message,), {

  'Characters' : _reflection.GeneratedProtocolMessageType('Characters', (_message.Message,), {
    'DESCRIPTOR' : _ENVSETTINGS_CHARACTERS,
    '__module__' : 'diambra.arena.engine.interface_pb2'
    # @@protoc_insertion_point(class_scope:interface.EnvSettings.Characters)
    })
  ,

  'SuperArts' : _reflection.GeneratedProtocolMessageType('SuperArts', (_message.Message,), {
    'DESCRIPTOR' : _ENVSETTINGS_SUPERARTS,
    '__module__' : 'diambra.arena.engine.interface_pb2'
    # @@protoc_insertion_point(class_scope:interface.EnvSettings.SuperArts)
    })
  ,

  'FightingStyles' : _reflection.GeneratedProtocolMessageType('FightingStyles', (_message.Message,), {
    'DESCRIPTOR' : _ENVSETTINGS_FIGHTINGSTYLES,
    '__module__' : 'diambra.arena.engine.interface_pb2'
    # @@protoc_insertion_point(class_scope:interface.EnvSettings.FightingStyles)
    })
  ,

  'UltimateStyle' : _reflection.GeneratedProtocolMessageType('UltimateStyle', (_message.Message,), {
    'DESCRIPTOR' : _ENVSETTINGS_ULTIMATESTYLE,
    '__module__' : 'diambra.arena.engine.interface_pb2'
    # @@protoc_insertion_point(class_scope:interface.EnvSettings.UltimateStyle)
    })
  ,

  'UltimateStyles' : _reflection.GeneratedProtocolMessageType('UltimateStyles', (_message.Message,), {
    'DESCRIPTOR' : _ENVSETTINGS_ULTIMATESTYLES,
    '__module__' : 'diambra.arena.engine.interface_pb2'
    # @@protoc_insertion_point(class_scope:interface.EnvSettings.UltimateStyles)
    })
  ,
  'DESCRIPTOR' : _ENVSETTINGS,
  '__module__' : 'diambra.arena.engine.interface_pb2'
  # @@protoc_insertion_point(class_scope:interface.EnvSettings)
  })
_sym_db.RegisterMessage(EnvSettings)
_sym_db.RegisterMessage(EnvSettings.Characters)
_sym_db.RegisterMessage(EnvSettings.SuperArts)
_sym_db.RegisterMessage(EnvSettings.FightingStyles)
_sym_db.RegisterMessage(EnvSettings.UltimateStyle)
_sym_db.RegisterMessage(EnvSettings.UltimateStyles)

EnvInitResponse = _reflection.GeneratedProtocolMessageType('EnvInitResponse', (_message.Message,), {

  'MoveAndAttackActions' : _reflection.GeneratedProtocolMessageType('MoveAndAttackActions', (_message.Message,), {
    'DESCRIPTOR' : _ENVINITRESPONSE_MOVEANDATTACKACTIONS,
    '__module__' : 'diambra.arena.engine.interface_pb2'
    # @@protoc_insertion_point(class_scope:interface.EnvInitResponse.MoveAndAttackActions)
    })
  ,

  'AvailableActions' : _reflection.GeneratedProtocolMessageType('AvailableActions', (_message.Message,), {
    'DESCRIPTOR' : _ENVINITRESPONSE_AVAILABLEACTIONS,
    '__module__' : 'diambra.arena.engine.interface_pb2'
    # @@protoc_insertion_point(class_scope:interface.EnvInitResponse.AvailableActions)
    })
  ,

  'Buttons' : _reflection.GeneratedProtocolMessageType('Buttons', (_message.Message,), {
    'DESCRIPTOR' : _ENVINITRESPONSE_BUTTONS,
    '__module__' : 'diambra.arena.engine.interface_pb2'
    # @@protoc_insertion_point(class_scope:interface.EnvInitResponse.Buttons)
    })
  ,

  'ButtonMapping' : _reflection.GeneratedProtocolMessageType('ButtonMapping', (_message.Message,), {
    'DESCRIPTOR' : _ENVINITRESPONSE_BUTTONMAPPING,
    '__module__' : 'diambra.arena.engine.interface_pb2'
    # @@protoc_insertion_point(class_scope:interface.EnvInitResponse.ButtonMapping)
    })
  ,

  'RamStatesEntry' : _reflection.GeneratedProtocolMessageType('RamStatesEntry', (_message.Message,), {
    'DESCRIPTOR' : _ENVINITRESPONSE_RAMSTATESENTRY,
    '__module__' : 'diambra.arena.engine.interface_pb2'
    # @@protoc_insertion_point(class_scope:interface.EnvInitResponse.RamStatesEntry)
    })
  ,
  'DESCRIPTOR' : _ENVINITRESPONSE,
  '__module__' : 'diambra.arena.engine.interface_pb2'
  # @@protoc_insertion_point(class_scope:interface.EnvInitResponse)
  })
_sym_db.RegisterMessage(EnvInitResponse)
_sym_db.RegisterMessage(EnvInitResponse.MoveAndAttackActions)
_sym_db.RegisterMessage(EnvInitResponse.AvailableActions)
_sym_db.RegisterMessage(EnvInitResponse.Buttons)
_sym_db.RegisterMessage(EnvInitResponse.ButtonMapping)
_sym_db.RegisterMessage(EnvInitResponse.RamStatesEntry)

Action = _reflection.GeneratedProtocolMessageType('Action', (_message.Message,), {
  'DESCRIPTOR' : _ACTION,
  '__module__' : 'diambra.arena.engine.interface_pb2'
  # @@protoc_insertion_point(class_scope:interface.Action)
  })
_sym_db.RegisterMessage(Action)

Actions = _reflection.GeneratedProtocolMessageType('Actions', (_message.Message,), {
  'DESCRIPTOR' : _ACTIONS,
  '__module__' : 'diambra.arena.engine.interface_pb2'
  # @@protoc_insertion_point(class_scope:interface.Actions)
  })
_sym_db.RegisterMessage(Actions)

Observation = _reflection.GeneratedProtocolMessageType('Observation', (_message.Message,), {

  'GameState' : _reflection.GeneratedProtocolMessageType('GameState', (_message.Message,), {
    'DESCRIPTOR' : _OBSERVATION_GAMESTATE,
    '__module__' : 'diambra.arena.engine.interface_pb2'
    # @@protoc_insertion_point(class_scope:interface.Observation.GameState)
    })
  ,

  'RamStatesEntry' : _reflection.GeneratedProtocolMessageType('RamStatesEntry', (_message.Message,), {
    'DESCRIPTOR' : _OBSERVATION_RAMSTATESENTRY,
    '__module__' : 'diambra.arena.engine.interface_pb2'
    # @@protoc_insertion_point(class_scope:interface.Observation.RamStatesEntry)
    })
  ,
  'DESCRIPTOR' : _OBSERVATION,
  '__module__' : 'diambra.arena.engine.interface_pb2'
  # @@protoc_insertion_point(class_scope:interface.Observation)
  })
_sym_db.RegisterMessage(Observation)
_sym_db.RegisterMessage(Observation.GameState)
_sym_db.RegisterMessage(Observation.RamStatesEntry)

_ENVSERVER = DESCRIPTOR.services_by_name['EnvServer']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\242\002\003HLW'
  _ENVINITRESPONSE_RAMSTATESENTRY._options = None
  _ENVINITRESPONSE_RAMSTATESENTRY._serialized_options = b'8\001'
  _OBSERVATION_RAMSTATESENTRY._options = None
  _OBSERVATION_RAMSTATESENTRY._serialized_options = b'8\001'
  _ACTIONSPACE._serialized_start=2773
  _ACTIONSPACE._serialized_end=2846
  _EMPTY._serialized_start=51
  _EMPTY._serialized_end=58
  _OUTFITS._serialized_start=60
  _OUTFITS._serialized_end=93
  _CUMULATIVEREWARDBOUNDS._serialized_start=95
  _CUMULATIVEREWARDBOUNDS._serialized_end=145
  _ACTIONSPACES._serialized_start=147
  _ACTIONSPACES._serialized_end=233
  _ATTACKBUTTONSCOMBINATIONS._serialized_start=235
  _ATTACKBUTTONSCOMBINATIONS._serialized_end=286
  _FRAMESHAPE._serialized_start=288
  _FRAMESHAPE._serialized_end=333
  _RAMSTATE._serialized_start=335
  _RAMSTATE._serialized_end=398
  _ERRORMESSAGE._serialized_start=400
  _ERRORMESSAGE._serialized_end=437
  _ENVSETTINGS._serialized_start=440
  _ENVSETTINGS._serialized_end=1424
  _ENVSETTINGS_CHARACTERS._serialized_start=1132
  _ENVSETTINGS_CHARACTERS._serialized_end=1168
  _ENVSETTINGS_SUPERARTS._serialized_start=1170
  _ENVSETTINGS_SUPERARTS._serialized_end=1205
  _ENVSETTINGS_FIGHTINGSTYLES._serialized_start=1207
  _ENVSETTINGS_FIGHTINGSTYLES._serialized_end=1247
  _ENVSETTINGS_ULTIMATESTYLE._serialized_start=1249
  _ENVSETTINGS_ULTIMATESTYLE._serialized_end=1306
  _ENVSETTINGS_ULTIMATESTYLES._serialized_start=1308
  _ENVSETTINGS_ULTIMATESTYLES._serialized_end=1424
  _ENVINITRESPONSE._serialized_start=1427
  _ENVINITRESPONSE._serialized_end=2280
  _ENVINITRESPONSE_MOVEANDATTACKACTIONS._serialized_start=1873
  _ENVINITRESPONSE_MOVEANDATTACKACTIONS._serialized_end=1927
  _ENVINITRESPONSE_AVAILABLEACTIONS._serialized_start=1930
  _ENVINITRESPONSE_AVAILABLEACTIONS._serialized_end=2117
  _ENVINITRESPONSE_BUTTONS._serialized_start=2119
  _ENVINITRESPONSE_BUTTONS._serialized_end=2160
  _ENVINITRESPONSE_BUTTONMAPPING._serialized_start=2162
  _ENVINITRESPONSE_BUTTONMAPPING._serialized_end=2209
  _ENVINITRESPONSE_RAMSTATESENTRY._serialized_start=2211
  _ENVINITRESPONSE_RAMSTATESENTRY._serialized_end=2280
  _ACTION._serialized_start=2282
  _ACTION._serialized_end=2320
  _ACTIONS._serialized_start=2322
  _ACTIONS._serialized_end=2393
  _OBSERVATION._serialized_start=2396
  _OBSERVATION._serialized_end=2771
  _OBSERVATION_GAMESTATE._serialized_start=2608
  _OBSERVATION_GAMESTATE._serialized_end=2700
  _OBSERVATION_RAMSTATESENTRY._serialized_start=2211
  _OBSERVATION_RAMSTATESENTRY._serialized_end=2280
  _ENVSERVER._serialized_start=2849
  _ENVSERVER._serialized_end=3244
# @@protoc_insertion_point(module_scope)
