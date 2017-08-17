from tutorial import ExampleService
from tutorial.ttypes import ExampleStruct


from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer


class ExampleServiceHandler:
    def __init__(self):
        self.values = 0

    def example_method(self, stuct):
	self.values += struct.num1
        return self.values

def main():
    handler = ExampleServiceHandler()
    processor = ExampleService.Processor(handler)
    transport = TSocket.TServerSocket(port=9090)
    tfactory = TTransport.TBufferedTransportFactory()
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)
    server.serve()
