# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import todo_pb2 as todo__pb2


class TodoServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.CreateTodo = channel.unary_unary(
        '/TodoService/CreateTodo',
        request_serializer=todo__pb2.Todo.SerializeToString,
        response_deserializer=todo__pb2.Todo.FromString,
        )
    self.UpdateTodo = channel.unary_unary(
        '/TodoService/UpdateTodo',
        request_serializer=todo__pb2.Todo.SerializeToString,
        response_deserializer=todo__pb2.Todo.FromString,
        )
    self.GetAllTodos = channel.unary_unary(
        '/TodoService/GetAllTodos',
        request_serializer=todo__pb2.EmptyRequest.SerializeToString,
        response_deserializer=todo__pb2.Todos.FromString,
        )
    self.GetTodo = channel.unary_unary(
        '/TodoService/GetTodo',
        request_serializer=todo__pb2.GetTodoId.SerializeToString,
        response_deserializer=todo__pb2.Todo.FromString,
        )


class TodoServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def CreateTodo(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UpdateTodo(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetAllTodos(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetTodo(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_TodoServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'CreateTodo': grpc.unary_unary_rpc_method_handler(
          servicer.CreateTodo,
          request_deserializer=todo__pb2.Todo.FromString,
          response_serializer=todo__pb2.Todo.SerializeToString,
      ),
      'UpdateTodo': grpc.unary_unary_rpc_method_handler(
          servicer.UpdateTodo,
          request_deserializer=todo__pb2.Todo.FromString,
          response_serializer=todo__pb2.Todo.SerializeToString,
      ),
      'GetAllTodos': grpc.unary_unary_rpc_method_handler(
          servicer.GetAllTodos,
          request_deserializer=todo__pb2.EmptyRequest.FromString,
          response_serializer=todo__pb2.Todos.SerializeToString,
      ),
      'GetTodo': grpc.unary_unary_rpc_method_handler(
          servicer.GetTodo,
          request_deserializer=todo__pb2.GetTodoId.FromString,
          response_serializer=todo__pb2.Todo.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'TodoService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
