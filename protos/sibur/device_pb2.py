# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos/sibur/device.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='protos/sibur/device.proto',
  package='protos',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x19protos/sibur/device.proto\x12\x06protos\"\x9f\x01\n\nDeviceInfo\x12\r\n\x05model\x18\x01 \x01(\x05\x12\x0f\n\x07version\x18\x02 \x01(\x05\x12\x1a\n\x04mode\x18\x03 \x01(\x0e\x32\x0c.protos.Mode\x12\x0e\n\x06period\x18\x04 \x01(\x05\x12\x0f\n\x07measure\x18\x05 \x01(\x05\x12\x0f\n\x07\x62\x61ttery\x18\x06 \x01(\x05\x12#\n\x04\x64\x61ta\x18\x07 \x03(\x0b\x32\x15.protos.PortData_info\"D\n\x11\x46romDeviceMessage\x12\x0f\n\x07\x62\x61ttery\x18\x01 \x01(\x05\x12\x1e\n\x04\x64\x61ta\x18\x02 \x03(\x0b\x32\x10.protos.PortData\"Y\n\x08PortData\x12 \n\x04port\x18\x01 \x01(\x0e\x32\x12.protos.DevicePort\x12\r\n\x05value\x18\x02 \x01(\x05\x12\x1c\n\x05\x65vent\x18\x03 \x01(\x0e\x32\r.protos.Event\"{\n\x08Messages\x12\x1d\n\x04type\x18\x01 \x01(\x0e\x32\x0f.protos.MsgType\x12$\n\x08\x64\x65v_info\x18\x02 \x01(\x0b\x32\x12.protos.DeviceInfo\x12*\n\x07\x64\x65v_msg\x18\x03 \x01(\x0b\x32\x19.protos.FromDeviceMessage\"Z\n\rPortData_info\x12 \n\x04port\x18\x01 \x01(\x0e\x32\x12.protos.DevicePort\x12\r\n\x05value\x18\x02 \x01(\x05\x12\x0b\n\x03min\x18\x03 \x01(\x05\x12\x0b\n\x03max\x18\x04 \x01(\x05\"p\n\x0fToDeviceMessage\x12\x1a\n\x04mode\x18\x01 \x01(\x0e\x32\x0c.protos.Mode\x12\x0e\n\x06period\x18\x02 \x01(\x05\x12\x0f\n\x07measure\x18\x03 \x01(\x05\x12 \n\x04port\x18\x04 \x03(\x0b\x32\x12.protos.ToPortData\"H\n\nToPortData\x12 \n\x04port\x18\x01 \x01(\x0e\x32\x12.protos.DevicePort\x12\x0b\n\x03min\x18\x02 \x01(\x05\x12\x0b\n\x03max\x18\x03 \x01(\x05\"\'\n\x04Sets\x12\x0e\n\x06switch\x18\x01 \x01(\x05\x12\x0f\n\x07measure\x18\x02 \x01(\x05\".\n\x0e\x44\x65viceFreqPlan\x12\x1c\n\x04\x66req\x18\x01 \x01(\x0e\x32\x0e.protos.Region*5\n\x04Mode\x12\n\n\x06PERIOD\x10\x00\x12\x0c\n\x08\x42OUNDARY\x10\x01\x12\x13\n\x0f\x42OUNDARY_PERIOD\x10\x02*-\n\x05\x45vent\x12\x10\n\x0cPERIOD_EVENT\x10\x00\x12\x12\n\x0e\x42OUNDARY_EVENT\x10\x01*P\n\nDevicePort\x12\x08\n\x04PORT\x10\x00\x12\t\n\x05VIBR1\x10\x01\x12\t\n\x05VIBR2\x10\x02\x12\n\n\x06TEMPL1\x10\x03\x12\n\n\x06TEMPL2\x10\x04\x12\n\n\x06TEMPH1\x10\x05*\x1d\n\x07MsgType\x12\t\n\x05SMALL\x10\x00\x12\x07\n\x03\x42IG\x10\x01*j\n\x06Region\x12\x08\n\x04ZERO\x10\x00\x12\t\n\x05RU868\x10\x01\x12\t\n\x05\x45U868\x10\x02\x12\t\n\x05IN865\x10\x03\x12\t\n\x05\x41S923\x10\x04\x12\t\n\x05\x41U915\x10\x05\x12\t\n\x05KR920\x10\x06\x12\t\n\x05US915\x10\x07\x12\t\n\x05KZ865\x10\x08\x62\x06proto3')
)

_MODE = _descriptor.EnumDescriptor(
  name='Mode',
  full_name='protos.Mode',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='PERIOD', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BOUNDARY', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BOUNDARY_PERIOD', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=854,
  serialized_end=907,
)
_sym_db.RegisterEnumDescriptor(_MODE)

Mode = enum_type_wrapper.EnumTypeWrapper(_MODE)
_EVENT = _descriptor.EnumDescriptor(
  name='Event',
  full_name='protos.Event',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='PERIOD_EVENT', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BOUNDARY_EVENT', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=909,
  serialized_end=954,
)
_sym_db.RegisterEnumDescriptor(_EVENT)

Event = enum_type_wrapper.EnumTypeWrapper(_EVENT)
_DEVICEPORT = _descriptor.EnumDescriptor(
  name='DevicePort',
  full_name='protos.DevicePort',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='PORT', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VIBR1', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VIBR2', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TEMPL1', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TEMPL2', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TEMPH1', index=5, number=5,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=956,
  serialized_end=1036,
)
_sym_db.RegisterEnumDescriptor(_DEVICEPORT)

DevicePort = enum_type_wrapper.EnumTypeWrapper(_DEVICEPORT)
_MSGTYPE = _descriptor.EnumDescriptor(
  name='MsgType',
  full_name='protos.MsgType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SMALL', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BIG', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1038,
  serialized_end=1067,
)
_sym_db.RegisterEnumDescriptor(_MSGTYPE)

MsgType = enum_type_wrapper.EnumTypeWrapper(_MSGTYPE)
_REGION = _descriptor.EnumDescriptor(
  name='Region',
  full_name='protos.Region',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ZERO', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RU868', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EU868', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='IN865', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AS923', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AU915', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='KR920', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='US915', index=7, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='KZ865', index=8, number=8,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1069,
  serialized_end=1175,
)
_sym_db.RegisterEnumDescriptor(_REGION)

Region = enum_type_wrapper.EnumTypeWrapper(_REGION)
PERIOD = 0
BOUNDARY = 1
BOUNDARY_PERIOD = 2
PERIOD_EVENT = 0
BOUNDARY_EVENT = 1
PORT = 0
VIBR1 = 1
VIBR2 = 2
TEMPL1 = 3
TEMPL2 = 4
TEMPH1 = 5
SMALL = 0
BIG = 1
ZERO = 0
RU868 = 1
EU868 = 2
IN865 = 3
AS923 = 4
AU915 = 5
KR920 = 6
US915 = 7
KZ865 = 8



_DEVICEINFO = _descriptor.Descriptor(
  name='DeviceInfo',
  full_name='protos.DeviceInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='model', full_name='protos.DeviceInfo.model', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='version', full_name='protos.DeviceInfo.version', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mode', full_name='protos.DeviceInfo.mode', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='period', full_name='protos.DeviceInfo.period', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='measure', full_name='protos.DeviceInfo.measure', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='battery', full_name='protos.DeviceInfo.battery', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='protos.DeviceInfo.data', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=38,
  serialized_end=197,
)


_FROMDEVICEMESSAGE = _descriptor.Descriptor(
  name='FromDeviceMessage',
  full_name='protos.FromDeviceMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='battery', full_name='protos.FromDeviceMessage.battery', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='protos.FromDeviceMessage.data', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=199,
  serialized_end=267,
)


_PORTDATA = _descriptor.Descriptor(
  name='PortData',
  full_name='protos.PortData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='port', full_name='protos.PortData.port', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='protos.PortData.value', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='event', full_name='protos.PortData.event', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=269,
  serialized_end=358,
)


_MESSAGES = _descriptor.Descriptor(
  name='Messages',
  full_name='protos.Messages',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='protos.Messages.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dev_info', full_name='protos.Messages.dev_info', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dev_msg', full_name='protos.Messages.dev_msg', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=360,
  serialized_end=483,
)


_PORTDATA_INFO = _descriptor.Descriptor(
  name='PortData_info',
  full_name='protos.PortData_info',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='port', full_name='protos.PortData_info.port', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='protos.PortData_info.value', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='min', full_name='protos.PortData_info.min', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max', full_name='protos.PortData_info.max', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=485,
  serialized_end=575,
)


_TODEVICEMESSAGE = _descriptor.Descriptor(
  name='ToDeviceMessage',
  full_name='protos.ToDeviceMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='mode', full_name='protos.ToDeviceMessage.mode', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='period', full_name='protos.ToDeviceMessage.period', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='measure', full_name='protos.ToDeviceMessage.measure', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='port', full_name='protos.ToDeviceMessage.port', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=577,
  serialized_end=689,
)


_TOPORTDATA = _descriptor.Descriptor(
  name='ToPortData',
  full_name='protos.ToPortData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='port', full_name='protos.ToPortData.port', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='min', full_name='protos.ToPortData.min', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max', full_name='protos.ToPortData.max', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=691,
  serialized_end=763,
)


_SETS = _descriptor.Descriptor(
  name='Sets',
  full_name='protos.Sets',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='switch', full_name='protos.Sets.switch', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='measure', full_name='protos.Sets.measure', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=765,
  serialized_end=804,
)


_DEVICEFREQPLAN = _descriptor.Descriptor(
  name='DeviceFreqPlan',
  full_name='protos.DeviceFreqPlan',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='freq', full_name='protos.DeviceFreqPlan.freq', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=806,
  serialized_end=852,
)

_DEVICEINFO.fields_by_name['mode'].enum_type = _MODE
_DEVICEINFO.fields_by_name['data'].message_type = _PORTDATA_INFO
_FROMDEVICEMESSAGE.fields_by_name['data'].message_type = _PORTDATA
_PORTDATA.fields_by_name['port'].enum_type = _DEVICEPORT
_PORTDATA.fields_by_name['event'].enum_type = _EVENT
_MESSAGES.fields_by_name['type'].enum_type = _MSGTYPE
_MESSAGES.fields_by_name['dev_info'].message_type = _DEVICEINFO
_MESSAGES.fields_by_name['dev_msg'].message_type = _FROMDEVICEMESSAGE
_PORTDATA_INFO.fields_by_name['port'].enum_type = _DEVICEPORT
_TODEVICEMESSAGE.fields_by_name['mode'].enum_type = _MODE
_TODEVICEMESSAGE.fields_by_name['port'].message_type = _TOPORTDATA
_TOPORTDATA.fields_by_name['port'].enum_type = _DEVICEPORT
_DEVICEFREQPLAN.fields_by_name['freq'].enum_type = _REGION
DESCRIPTOR.message_types_by_name['DeviceInfo'] = _DEVICEINFO
DESCRIPTOR.message_types_by_name['FromDeviceMessage'] = _FROMDEVICEMESSAGE
DESCRIPTOR.message_types_by_name['PortData'] = _PORTDATA
DESCRIPTOR.message_types_by_name['Messages'] = _MESSAGES
DESCRIPTOR.message_types_by_name['PortData_info'] = _PORTDATA_INFO
DESCRIPTOR.message_types_by_name['ToDeviceMessage'] = _TODEVICEMESSAGE
DESCRIPTOR.message_types_by_name['ToPortData'] = _TOPORTDATA
DESCRIPTOR.message_types_by_name['Sets'] = _SETS
DESCRIPTOR.message_types_by_name['DeviceFreqPlan'] = _DEVICEFREQPLAN
DESCRIPTOR.enum_types_by_name['Mode'] = _MODE
DESCRIPTOR.enum_types_by_name['Event'] = _EVENT
DESCRIPTOR.enum_types_by_name['DevicePort'] = _DEVICEPORT
DESCRIPTOR.enum_types_by_name['MsgType'] = _MSGTYPE
DESCRIPTOR.enum_types_by_name['Region'] = _REGION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DeviceInfo = _reflection.GeneratedProtocolMessageType('DeviceInfo', (_message.Message,), dict(
  DESCRIPTOR = _DEVICEINFO,
  __module__ = 'protos.sibur.device_pb2'
  # @@protoc_insertion_point(class_scope:protos.DeviceInfo)
  ))
_sym_db.RegisterMessage(DeviceInfo)

FromDeviceMessage = _reflection.GeneratedProtocolMessageType('FromDeviceMessage', (_message.Message,), dict(
  DESCRIPTOR = _FROMDEVICEMESSAGE,
  __module__ = 'protos.sibur.device_pb2'
  # @@protoc_insertion_point(class_scope:protos.FromDeviceMessage)
  ))
_sym_db.RegisterMessage(FromDeviceMessage)

PortData = _reflection.GeneratedProtocolMessageType('PortData', (_message.Message,), dict(
  DESCRIPTOR = _PORTDATA,
  __module__ = 'protos.sibur.device_pb2'
  # @@protoc_insertion_point(class_scope:protos.PortData)
  ))
_sym_db.RegisterMessage(PortData)

Messages = _reflection.GeneratedProtocolMessageType('Messages', (_message.Message,), dict(
  DESCRIPTOR = _MESSAGES,
  __module__ = 'protos.sibur.device_pb2'
  # @@protoc_insertion_point(class_scope:protos.Messages)
  ))
_sym_db.RegisterMessage(Messages)

PortData_info = _reflection.GeneratedProtocolMessageType('PortData_info', (_message.Message,), dict(
  DESCRIPTOR = _PORTDATA_INFO,
  __module__ = 'protos.sibur.device_pb2'
  # @@protoc_insertion_point(class_scope:protos.PortData_info)
  ))
_sym_db.RegisterMessage(PortData_info)

ToDeviceMessage = _reflection.GeneratedProtocolMessageType('ToDeviceMessage', (_message.Message,), dict(
  DESCRIPTOR = _TODEVICEMESSAGE,
  __module__ = 'protos.sibur.device_pb2'
  # @@protoc_insertion_point(class_scope:protos.ToDeviceMessage)
  ))
_sym_db.RegisterMessage(ToDeviceMessage)

ToPortData = _reflection.GeneratedProtocolMessageType('ToPortData', (_message.Message,), dict(
  DESCRIPTOR = _TOPORTDATA,
  __module__ = 'protos.sibur.device_pb2'
  # @@protoc_insertion_point(class_scope:protos.ToPortData)
  ))
_sym_db.RegisterMessage(ToPortData)

Sets = _reflection.GeneratedProtocolMessageType('Sets', (_message.Message,), dict(
  DESCRIPTOR = _SETS,
  __module__ = 'protos.sibur.device_pb2'
  # @@protoc_insertion_point(class_scope:protos.Sets)
  ))
_sym_db.RegisterMessage(Sets)

DeviceFreqPlan = _reflection.GeneratedProtocolMessageType('DeviceFreqPlan', (_message.Message,), dict(
  DESCRIPTOR = _DEVICEFREQPLAN,
  __module__ = 'protos.sibur.device_pb2'
  # @@protoc_insertion_point(class_scope:protos.DeviceFreqPlan)
  ))
_sym_db.RegisterMessage(DeviceFreqPlan)


# @@protoc_insertion_point(module_scope)
