import example_pb2

def run_example():
 person = example_pb2.Person()
 person.id = 5
 serialized_string = person.SerializeToString()
 new_person = example_pb2.Person() 
 new_person.ParseFromString(serialized_string)
 assert(new_person.id == 5)
