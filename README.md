TODO with grpc 

python -m grpc_tools.protoc -I ./ --python_out=. --grpc_python_out=. ./todo.proto