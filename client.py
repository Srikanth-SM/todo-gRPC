import grpc
from todo_pb2_grpc import TodoServiceStub
from todo_pb2 import Todo, EmptyRequest, GetTodoId

channel = grpc.insecure_channel('localhost:50051')
stub = TodoServiceStub(channel)

print(stub.CreateTodo(Todo(id=23, todo_text="yahoo")))
print(stub.CreateTodo(Todo(id=25, todo_text="need to attend the meeting")))

todo = stub.GetTodo(GetTodoId(id=23))
print(todo)
todo.status = 1
todow = stub.UpdateTodo(todo)
print(todow)
