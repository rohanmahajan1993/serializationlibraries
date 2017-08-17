from examples import ExampleService
from tutorial.ttypes import struct

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol


def main():
    # Make socket
    transport = TSocket.TSocket('localhost', 9090)

    # Buffering is critical. Raw sockets are very slow
    transport = TTransport.TBufferedTransport(transport)

    # Wrap in a protocol
    protocol = TBinaryProtocol.TBinaryProtocol(transport)

    # Create a client to use the protocol encoder
    client = ExampleService.Client(protocol)

    # Connect!
    transport.open()
    struct = ExampleStruct()
    struct.num1 = 55
    result = client.example_method(struct)
    print "the result was", result
    transport.close()
