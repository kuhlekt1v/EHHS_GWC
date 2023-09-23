# QUICK INTRODUCTION TO OBJECT ORIENTED PROGRAMMING

# - There are 2 types of programming.
#	1. Procedural programming - what we have been doing with the functions
#	2. Objected Oriented Programming - Advanced concept, but in general
#		we combine groups of related functions & variables into units called
#		objects
#		
#		Variables - called properties
#		Functions - called methods
		
#	Example- 
#		CAR
#		-----------
#		  make		|
#		  model		properties
#		  color		|
#		  ______________
#		  start()	|
#		  stop()	methods
#		  idle()	|
		  
class Car:
    def __init__(self, make, model, color):
        self.make = make
        self.model = model
        self.color = color

    def start(self):
        print("The {} is now started!")
        #print("The {} is now started!".format(self.make))

new_car = Car("toyota", "camry", "red")
print(new_car.make)
new_car.start()

another_car = Car("ford", "prius", "blue")
print(another_car.make)
another_car.start()	  

