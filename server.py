import sys
import time
import logging
from functools import wraps

import grpc
from concurrent import futures
from todo_pb2 import (Todo, Todos)
from todo_pb2_grpc import (TodoServiceServicer,
                           add_TodoServiceServicer_to_server)

from database.models import Todo
from database.models import session
import todo_pb2


log_format = '%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s'
logging.basicConfig(
    stream=sys.stdout, level=logging.DEBUG,
    format=log_format, datefmt="%Y-%m-%d %H:%M:%S"
)


def log_request(function):
    @wraps(function)
    def inner_function(*args, **kwargs):
        logging.info("received request: {}".format(function.__name__))
        resp = function(*args, **kwargs)
        return resp
    return inner_function


class TodoServiceServicer(TodoServiceServicer):

    @log_request
    def CreateTodo(self, request, context):
        # todo_response = Todo()
        try:
            if request.todo_text:
                todo = Todo(
                            todo_text=request.todo_text)
                session.add(todo)
                session.commit()
                todo_response = todo.asdict()
                return todo_pb2.Todo(**todo_response)
            else:
                raise ValueError("todo text must be present")
        except Exception as e:
            print("Exception occured,{0}".format(e.__str__()))
            return Todo()

    @log_request
    def GetAllTodos(self, request, context):
        todos = []
        try:
            todos = session.query(Todo).all()
            todos_response = []
            for todo in todos:
                todos_response.append(todo_pb2.Todo(**todo.asdict()))

            return todo_pb2.Todos(todos=todos_response)
        except Exception as e:
            print("Exception occured,{0}".format(e.__str__()))
            return Todos()

    @log_request
    def GetTodo(self, request, context):
        try:
            if not request.id:
                raise ValueError("id must be present")
            todo = session.query(Todo).get(request.id)
            return todo_pb2.Todo(**todo.asdict())
        except Exception as e:
            print("Exception occured,{0}".format(e.__str__()))
            return Todo()

    @log_request
    def UpdateTodo(self, request, context):

        try:
            if not request.id:
                raise ValueError("id must be present")
            todo = session.query(Todo).filter(
                Todo.id == request.id).update({'status': request.status})
            session.commit()
            return todo_pb2.Todo(**(session.query(Todo).get(request.id).asdict()))
        except Exception as e:
            print("Exception occured,{0}".format(e.__str__()))
            return Todo()
    
    
    @log_request
    def DeleteTodo(self,request,context):
        try:
            if not request.id:
                raise ValueError("id must be present")
            todo = session.query(Todo).filter(Todo.id==request.id)
            todo.delete(synchronize_session=False)
            logging.info("hai")
            logging.info(todo)
            session.commit()
            return todo_pb2.EmptyRequest()
        except Exception as e:
            print("Exception occured,{0}".format(e.__str__()))
            return Todo()



server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

add_TodoServiceServicer_to_server(
    TodoServiceServicer(), server)


print('Starting server. Listening on port 50051.')
server.add_insecure_port('[::]:50051')
server.start()


try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)
