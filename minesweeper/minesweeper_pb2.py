# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: minesweeper.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='minesweeper.proto',
  package='proto',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x11minesweeper.proto\x12\x05proto\"\x10\n\x0eNewGameRequest\"\'\n\x08Position\x12\x0b\n\x03row\x18\x01 \x01(\x05\x12\x0e\n\x06\x63olumn\x18\x02 \x01(\x05\"1\n\x0fNewGameResponse\x12\x0f\n\x07levelID\x18\x01 \x01(\t\x12\r\n\x05\x65rror\x18\x02 \x01(\t\"$\n\x11StartLevelRequest\x12\x0f\n\x07levelID\x18\x01 \x01(\t\"Q\n\x12StartLevelResponse\x12\x0c\n\x04Rows\x18\x01 \x01(\x05\x12\x0f\n\x07\x43olumns\x18\x02 \x01(\x05\x12\r\n\x05Mines\x18\x03 \x01(\x05\x12\r\n\x05\x65rror\x18\x04 \x01(\t\">\n\x0c\x43lickRequest\x12\x0f\n\x07levelID\x18\x01 \x01(\t\x12\x1d\n\x04tile\x18\x02 \x01(\x0b\x32\x0f.proto.Position\"-\n\rClickResponse\x12\r\n\x05value\x18\x01 \x01(\x05\x12\r\n\x05\x65rror\x18\x02 \x01(\t\"D\n\x11SolveLevelRequest\x12\x0f\n\x07levelID\x18\x01 \x01(\t\x12\x1e\n\x05mines\x18\x02 \x03(\x0b\x32\x0f.proto.Position\"F\n\x12SolveLevelResponse\x12\x13\n\x0bnextLevelID\x18\x01 \x01(\t\x12\x0c\n\x04\x66lag\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t2\x81\x02\n\x0bMinesweeper\x12\x38\n\x07NewGame\x12\x15.proto.NewGameRequest\x1a\x16.proto.NewGameResponse\x12\x41\n\nStartLevel\x12\x18.proto.StartLevelRequest\x1a\x19.proto.StartLevelResponse\x12\x32\n\x05\x43lick\x12\x13.proto.ClickRequest\x1a\x14.proto.ClickResponse\x12\x41\n\nSolveLevel\x12\x18.proto.SolveLevelRequest\x1a\x19.proto.SolveLevelResponseb\x06proto3'
)




_NEWGAMEREQUEST = _descriptor.Descriptor(
  name='NewGameRequest',
  full_name='proto.NewGameRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=28,
  serialized_end=44,
)


_POSITION = _descriptor.Descriptor(
  name='Position',
  full_name='proto.Position',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='row', full_name='proto.Position.row', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='column', full_name='proto.Position.column', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=46,
  serialized_end=85,
)


_NEWGAMERESPONSE = _descriptor.Descriptor(
  name='NewGameResponse',
  full_name='proto.NewGameResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='levelID', full_name='proto.NewGameResponse.levelID', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='error', full_name='proto.NewGameResponse.error', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=87,
  serialized_end=136,
)


_STARTLEVELREQUEST = _descriptor.Descriptor(
  name='StartLevelRequest',
  full_name='proto.StartLevelRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='levelID', full_name='proto.StartLevelRequest.levelID', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=138,
  serialized_end=174,
)


_STARTLEVELRESPONSE = _descriptor.Descriptor(
  name='StartLevelResponse',
  full_name='proto.StartLevelResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='Rows', full_name='proto.StartLevelResponse.Rows', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Columns', full_name='proto.StartLevelResponse.Columns', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Mines', full_name='proto.StartLevelResponse.Mines', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='error', full_name='proto.StartLevelResponse.error', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=176,
  serialized_end=257,
)


_CLICKREQUEST = _descriptor.Descriptor(
  name='ClickRequest',
  full_name='proto.ClickRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='levelID', full_name='proto.ClickRequest.levelID', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tile', full_name='proto.ClickRequest.tile', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=259,
  serialized_end=321,
)


_CLICKRESPONSE = _descriptor.Descriptor(
  name='ClickResponse',
  full_name='proto.ClickResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='proto.ClickResponse.value', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='error', full_name='proto.ClickResponse.error', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=323,
  serialized_end=368,
)


_SOLVELEVELREQUEST = _descriptor.Descriptor(
  name='SolveLevelRequest',
  full_name='proto.SolveLevelRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='levelID', full_name='proto.SolveLevelRequest.levelID', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='mines', full_name='proto.SolveLevelRequest.mines', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=370,
  serialized_end=438,
)


_SOLVELEVELRESPONSE = _descriptor.Descriptor(
  name='SolveLevelResponse',
  full_name='proto.SolveLevelResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='nextLevelID', full_name='proto.SolveLevelResponse.nextLevelID', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='flag', full_name='proto.SolveLevelResponse.flag', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='error', full_name='proto.SolveLevelResponse.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=440,
  serialized_end=510,
)

_CLICKREQUEST.fields_by_name['tile'].message_type = _POSITION
_SOLVELEVELREQUEST.fields_by_name['mines'].message_type = _POSITION
DESCRIPTOR.message_types_by_name['NewGameRequest'] = _NEWGAMEREQUEST
DESCRIPTOR.message_types_by_name['Position'] = _POSITION
DESCRIPTOR.message_types_by_name['NewGameResponse'] = _NEWGAMERESPONSE
DESCRIPTOR.message_types_by_name['StartLevelRequest'] = _STARTLEVELREQUEST
DESCRIPTOR.message_types_by_name['StartLevelResponse'] = _STARTLEVELRESPONSE
DESCRIPTOR.message_types_by_name['ClickRequest'] = _CLICKREQUEST
DESCRIPTOR.message_types_by_name['ClickResponse'] = _CLICKRESPONSE
DESCRIPTOR.message_types_by_name['SolveLevelRequest'] = _SOLVELEVELREQUEST
DESCRIPTOR.message_types_by_name['SolveLevelResponse'] = _SOLVELEVELRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

NewGameRequest = _reflection.GeneratedProtocolMessageType('NewGameRequest', (_message.Message,), {
  'DESCRIPTOR' : _NEWGAMEREQUEST,
  '__module__' : 'minesweeper_pb2'
  # @@protoc_insertion_point(class_scope:proto.NewGameRequest)
  })
_sym_db.RegisterMessage(NewGameRequest)

Position = _reflection.GeneratedProtocolMessageType('Position', (_message.Message,), {
  'DESCRIPTOR' : _POSITION,
  '__module__' : 'minesweeper_pb2'
  # @@protoc_insertion_point(class_scope:proto.Position)
  })
_sym_db.RegisterMessage(Position)

NewGameResponse = _reflection.GeneratedProtocolMessageType('NewGameResponse', (_message.Message,), {
  'DESCRIPTOR' : _NEWGAMERESPONSE,
  '__module__' : 'minesweeper_pb2'
  # @@protoc_insertion_point(class_scope:proto.NewGameResponse)
  })
_sym_db.RegisterMessage(NewGameResponse)

StartLevelRequest = _reflection.GeneratedProtocolMessageType('StartLevelRequest', (_message.Message,), {
  'DESCRIPTOR' : _STARTLEVELREQUEST,
  '__module__' : 'minesweeper_pb2'
  # @@protoc_insertion_point(class_scope:proto.StartLevelRequest)
  })
_sym_db.RegisterMessage(StartLevelRequest)

StartLevelResponse = _reflection.GeneratedProtocolMessageType('StartLevelResponse', (_message.Message,), {
  'DESCRIPTOR' : _STARTLEVELRESPONSE,
  '__module__' : 'minesweeper_pb2'
  # @@protoc_insertion_point(class_scope:proto.StartLevelResponse)
  })
_sym_db.RegisterMessage(StartLevelResponse)

ClickRequest = _reflection.GeneratedProtocolMessageType('ClickRequest', (_message.Message,), {
  'DESCRIPTOR' : _CLICKREQUEST,
  '__module__' : 'minesweeper_pb2'
  # @@protoc_insertion_point(class_scope:proto.ClickRequest)
  })
_sym_db.RegisterMessage(ClickRequest)

ClickResponse = _reflection.GeneratedProtocolMessageType('ClickResponse', (_message.Message,), {
  'DESCRIPTOR' : _CLICKRESPONSE,
  '__module__' : 'minesweeper_pb2'
  # @@protoc_insertion_point(class_scope:proto.ClickResponse)
  })
_sym_db.RegisterMessage(ClickResponse)

SolveLevelRequest = _reflection.GeneratedProtocolMessageType('SolveLevelRequest', (_message.Message,), {
  'DESCRIPTOR' : _SOLVELEVELREQUEST,
  '__module__' : 'minesweeper_pb2'
  # @@protoc_insertion_point(class_scope:proto.SolveLevelRequest)
  })
_sym_db.RegisterMessage(SolveLevelRequest)

SolveLevelResponse = _reflection.GeneratedProtocolMessageType('SolveLevelResponse', (_message.Message,), {
  'DESCRIPTOR' : _SOLVELEVELRESPONSE,
  '__module__' : 'minesweeper_pb2'
  # @@protoc_insertion_point(class_scope:proto.SolveLevelResponse)
  })
_sym_db.RegisterMessage(SolveLevelResponse)



_MINESWEEPER = _descriptor.ServiceDescriptor(
  name='Minesweeper',
  full_name='proto.Minesweeper',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=513,
  serialized_end=770,
  methods=[
  _descriptor.MethodDescriptor(
    name='NewGame',
    full_name='proto.Minesweeper.NewGame',
    index=0,
    containing_service=None,
    input_type=_NEWGAMEREQUEST,
    output_type=_NEWGAMERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='StartLevel',
    full_name='proto.Minesweeper.StartLevel',
    index=1,
    containing_service=None,
    input_type=_STARTLEVELREQUEST,
    output_type=_STARTLEVELRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Click',
    full_name='proto.Minesweeper.Click',
    index=2,
    containing_service=None,
    input_type=_CLICKREQUEST,
    output_type=_CLICKRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='SolveLevel',
    full_name='proto.Minesweeper.SolveLevel',
    index=3,
    containing_service=None,
    input_type=_SOLVELEVELREQUEST,
    output_type=_SOLVELEVELRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_MINESWEEPER)

DESCRIPTOR.services_by_name['Minesweeper'] = _MINESWEEPER

# @@protoc_insertion_point(module_scope)
