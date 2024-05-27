from dataclasses import dataclass

@dataclass
class Person:
    name:str
    age:int
    profession:str

person1 = Person('Sahil',24,'DS')
person1
person1.age