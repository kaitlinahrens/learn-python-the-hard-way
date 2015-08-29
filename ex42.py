## Animal is-a object
class Animal(object):
	pass

## Dog is-a Animal
class Dog(Animal):

	def __init__(self, name):
		## A self has-a name? What?
		self.name = name

## Cat is-a Animal
class Cat(Animal):

	def __init__(self, name):
		## Self has-a name? I don't understand what is supposed to go here 
		self.name = name

## Person is-a object
class Person(object):

	def __init__(self, name):
		## A self has-a name, sure 
		self.name = name

		## Person has-a pet of some kind
		self.pet = None

## Employee is-a person
class Employee(Person):

	def __init__(self, name, salary):
		## ?? Whaaaaaaaaaaat
		super(Employee, self).__init__(name)
		## a person has a salary?


## fish is-a object
class Fish(object):
	pass

## Salmon is-a fish
class Salmon(fish):
	pass

## Halibut is-a fish
class Halibut(fish):
	pass


## rover is-a Dog
rover = Dog("Rover")

## satan is-a Cat
satan = Cat("Satan")

## mary is-a Person
mary = Person("Mary")

## mary has-a satan. satan is-a cat
mary.pet = satan

## Frank is-a employee. frank has-a salary of 120000
frank = Employee("Frank", 120000)

## frank has-a rover. rover is-a pet
frank.pet = rover

## flipper is-a fish
flipper = Fish()

## crouse is-a salmon
crouse = Salmon()

## harry is-a halibut
harry = Halibut()

# help































