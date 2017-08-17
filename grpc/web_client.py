import grpc

import example_pb2
import example_pb2_grpc


def run():
  channel = grpc.insecure_channel('localhost:50051')
  stub = example_pb2_grpc.ExampleServiceStub(channel)
  response = stub.ExampleMethod(example_pb2.ExampleRequest(name='you'))
  print("Greeter client received: " + response.name)
run()
