struct ExampleStruct {
  1: i32 num1 = 0,
}

service ExampleService {
   i32 example_method(1: ExampleStruct example) 
}




