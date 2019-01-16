import grpc
from todo_pb2_grpc import TodoServiceStub
from todo_pb2 import Todo, EmptyRequest

channel = grpc.insecure_channel('localhost:50051')
stub = TodoServiceStub(channel)

# print(stub.CreateTodo((todo_text="yahooss")))
print(stub.CreateTodo(Todo(todo_text="bu2 apple")))

todo = stub.GetTodo(Todo(id=8))
print(todo)
todo.status = 1
todow = stub.UpdateTodo(todo)
print(todow)
