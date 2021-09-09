# ASSIGNMENT: The below is a common design pattern that can be cleaned up.
# We have a lengthy mathematical operation that uses a few pieces of
# information several times in order to mutate a value. This code organization
# isn't inherently wrong, but it does result in some pretty messy callsites,
# especially once we introduce nested function calls in compound_op_it().
# 
# The goal of this assignment is to refactor the below into a class: 
# 1) Shared arguments between functions should become instance variables of the class
# in order to minimize clutter (because now they won't have to be arguments
# to each function). 
# 2) The class should have a function self.complicated_math_operation()
# that accomplishes everything complicated_math_operation() currently does.
# 3) There's a design decision lurking in here! Should we make the starting_value
# an instance variable of the class that each function call mutates, or should we
# keep the current structure where complicated_math_operation() accepts a starting value
# and repeatedly mutates it? Leave a comment explaining which one you chose
# and under what circumstances that might make sense. There's no right answer! 

#I cannot think of a reason why creating an instance variable might be any more efficient 
#for starting_value. It can be the idea of it updating constantly might be a problem. 
#We might want it to be more clear as of what the variable is doing through out the code.
#If it were me, I would keep it the way it is, but as I stated before it might be better to create
#an instance variable but I really don't know if that is a good/valid reason.

#Not only that, I really want to go over this code in class if possible. 

import math

def complicated_math_operation(self, min_value, max_value, coefficient):
    res = starting_value
    res = self.multiply_it(res)
    res = self.add_it(res)
    res = self.sqrt_it(res)
    res = self.compound_op_it(res)
    return res

def multiply_it(self, min_value, max_value, coefficient):
    return max(self.min_value, min(self.max_value, starting_value * self.coefficient))

def add_it(self, min_value, max_value, coefficient):
    return max(self.min_value, min(self.max_value, starting_value + self.coefficient))
 
def sqrt_it(self, min_value, max_value, coefficient):
    return max(self.min_value, min(self.max_value, math.pow(starting_value, -self.coefficient)))

def compound_op_it(self, self.min_value, self.max_value, self.coefficient):
    return self.add_it(self.multiply_it(starting_value)

def complicated_math_operation(self, min_value, max_value, coefficient):
    self.min_value = min_value
    self.max_value = max_value
    self.coefficient = coefficient
