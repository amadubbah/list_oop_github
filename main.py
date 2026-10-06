# person class(creating a class)
class Person:
    def __init__(self, name, age, person_id, height, gender, program): 
        self.name = name
        self.age = age
        self.person_id = person_id
        self.height = height
        self.gender = gender
        self.program = program


    def print_bio(self):
       print("Printing Person Details")
       print(f"Name: {self.name}")
       print(f"Age: {self.age}")
       print(f"ID: {self.person_id}")
       print(f"Height: {self.height}")
       print(f"Gender: {self.gender}")
       print(f"Proram: {self.program}")
       print("==========================")



# person object(creating a objects)
person1 = Person("Sidigue", 45, 5246, 5.9, "Male", "BSEM")
person2 = Person("Amadu", 21, 5866, 5.7, "Male", "BSEM") 
person3 = Person("Borboh", 22, 1011, 5.8, "Male", "BSEM")

person1.print_bio()
person2.print_bio()
person3.print_bio()
