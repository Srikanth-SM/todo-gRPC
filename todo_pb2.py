# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: todo.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='todo.proto',
  package='',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\ntodo.proto\"\x8d\x01\n\x04Todo\x12\n\n\x02id\x18\x01 \x02(\x05\x12\x11\n\ttodo_text\x18\x02 \x02(\t\x12\x12\n\ncreated_at\x18\x03 \x01(\x03\x12\x1c\n\x06status\x18\x04 \x01(\x0e\x32\x0c.Todo.Status\"4\n\x06Status\x12\x0e\n\nINPROGRESS\x10\x00\x12\r\n\tCOMPLETED\x10\x01\x12\x0b\n\x07\x43REATED\x10\x02\"\x17\n\tGetTodoId\x12\n\n\x02id\x18\x01 \x02(\x05\"\x1d\n\x05Todos\x12\x14\n\x05todos\x18\x01 \x03(\x0b\x32\x05.Todo\"\x0e\n\x0c\x45mptyRequest2\x91\x01\n\x0bTodoService\x12\x1c\n\nCreateTodo\x12\x05.Todo\x1a\x05.Todo\"\x00\x12\x1c\n\nUpdateTodo\x12\x05.Todo\x1a\x05.Todo\"\x00\x12&\n\x0bGetAllTodos\x12\r.EmptyRequest\x1a\x06.Todos\"\x00\x12\x1e\n\x07GetTodo\x12\n.GetTodoId\x1a\x05.Todo\"\x00')
)



_TODO_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='Todo.Status',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='INPROGRESS', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COMPLETED', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CREATED', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=104,
  serialized_end=156,
)
_sym_db.RegisterEnumDescriptor(_TODO_STATUS)


_TODO = _descriptor.Descriptor(
  name='Todo',
  full_name='Todo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='Todo.id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='todo_text', full_name='Todo.todo_text', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='created_at', full_name='Todo.created_at', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='Todo.status', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _TODO_STATUS,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=15,
  serialized_end=156,
)


_GETTODOID = _descriptor.Descriptor(
  name='GetTodoId',
  full_name='GetTodoId',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='GetTodoId.id', index=0,
      number=1, type=5, cpp_type=1, label=2,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=158,
  serialized_end=181,
)


_TODOS = _descriptor.Descriptor(
  name='Todos',
  full_name='Todos',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='todos', full_name='Todos.todos', index=0,
      number=1, type=11, cpp_type=10, label=3,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=183,
  serialized_end=212,
)


_EMPTYREQUEST = _descriptor.Descriptor(
  name='EmptyRequest',
  full_name='EmptyRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=214,
  serialized_end=228,
)

_TODO.fields_by_name['status'].enum_type = _TODO_STATUS
_TODO_STATUS.containing_type = _TODO
_TODOS.fields_by_name['todos'].message_type = _TODO
DESCRIPTOR.message_types_by_name['Todo'] = _TODO
DESCRIPTOR.message_types_by_name['GetTodoId'] = _GETTODOID
DESCRIPTOR.message_types_by_name['Todos'] = _TODOS
DESCRIPTOR.message_types_by_name['EmptyRequest'] = _EMPTYREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Todo = _reflection.GeneratedProtocolMessageType('Todo', (_message.Message,), dict(
  DESCRIPTOR = _TODO,
  __module__ = 'todo_pb2'
  # @@protoc_insertion_point(class_scope:Todo)
  ))
_sym_db.RegisterMessage(Todo)

GetTodoId = _reflection.GeneratedProtocolMessageType('GetTodoId', (_message.Message,), dict(
  DESCRIPTOR = _GETTODOID,
  __module__ = 'todo_pb2'
  # @@protoc_insertion_point(class_scope:GetTodoId)
  ))
_sym_db.RegisterMessage(GetTodoId)

Todos = _reflection.GeneratedProtocolMessageType('Todos', (_message.Message,), dict(
  DESCRIPTOR = _TODOS,
  __module__ = 'todo_pb2'
  # @@protoc_insertion_point(class_scope:Todos)
  ))
_sym_db.RegisterMessage(Todos)

EmptyRequest = _reflection.GeneratedProtocolMessageType('EmptyRequest', (_message.Message,), dict(
  DESCRIPTOR = _EMPTYREQUEST,
  __module__ = 'todo_pb2'
  # @@protoc_insertion_point(class_scope:EmptyRequest)
  ))
_sym_db.RegisterMessage(EmptyRequest)



_TODOSERVICE = _descriptor.ServiceDescriptor(
  name='TodoService',
  full_name='TodoService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=231,
  serialized_end=376,
  methods=[
  _descriptor.MethodDescriptor(
    name='CreateTodo',
    full_name='TodoService.CreateTodo',
    index=0,
    containing_service=None,
    input_type=_TODO,
    output_type=_TODO,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='UpdateTodo',
    full_name='TodoService.UpdateTodo',
    index=1,
    containing_service=None,
    input_type=_TODO,
    output_type=_TODO,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetAllTodos',
    full_name='TodoService.GetAllTodos',
    index=2,
    containing_service=None,
    input_type=_EMPTYREQUEST,
    output_type=_TODOS,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetTodo',
    full_name='TodoService.GetTodo',
    index=3,
    containing_service=None,
    input_type=_GETTODOID,
    output_type=_TODO,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_TODOSERVICE)

DESCRIPTOR.services_by_name['TodoService'] = _TODOSERVICE

# @@protoc_insertion_point(module_scope)
