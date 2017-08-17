import grpc
import time 

import example_pb2
import example_pb2_grpc

from concurrent import futures

class Example(example_pb2_grpc.ExampleServiceServicer):
   def ExampleMethod(self, request, context):
     return example_pb2.ExampleReply(name='Hello, %s!' % request.name)

def serve():
  server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
  example_pb2_grpc.add_ExampleServiceServicer_to_server(Example(), server)
  server.add_insecure_port('[::]:50051')
  server.start()
  try:
    while True:
      time.sleep(10000)
  except KeyboardInterrupt:
    server.stop(0)
serve()
