# class
# attributes
# methods

# abstraction 
# polymorphism
# inheritance
# encapsulation

# class car

    #width
    #height
    #color
    #engine_type
    #brand
    #model
    #year

#       def model x
#       def model y
#       def model 3

# Simple Calculator class

#Calculator.subract(2,1,4)

class Calculator:
    def __init__(self, num1, num2, num3):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3
        
    def add(self, num4):
        return self.num1 + self.num2 + self.num3 + num4
    
    def subtract(self):
        return self.num1 - self.num2
    
    def multiply(self):
        return self.num1 * self.num2 * self.num3
    
    def divide(self):
        return self.num1 / self.num2
