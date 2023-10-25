from numpy import random
import numpy as np

#generate random integers
x=random.randint(10) #prints from [0,100)
print(x)
arr=random.randint(10,size=(4))
print(arr)

#generate random floating point number from 0 to 1
y=random.rand()
print(y)
z=random.rand(4)
print(z)

#The choice() method allows you to generate a random value based on an array of values.
#The choice() method takes an array as a parameter and randomly returns one of the values.
a=random.choice(arr)
print(a)
b=random.choice([1,3,5,7])
print(b)
c=random.choice([1,2,4,6,7,4],size=(2,1))
print(c)

#shuffling
random.shuffle(arr)
print(arr)
#shuffle makes changes to the original array whereas permuation returns a re-arranged array
