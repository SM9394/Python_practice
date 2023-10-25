#Slicing in python means taking elements from one given index to another given index.
#We pass slice instead of index like this: [start:end].
#We can also define the step, like this: [start:end:step].
#If we don't pass start its considered 0
#If we don't pass end its considered length of array in that dimension
#If we don't pass step its considered 1

import numpy as np

arr=np.array([1,2,3,4,5,6,7])
print(arr[0:4]) #returns arr[0] to arr[4]
print(arr[0:-2]) #returns arr[0] to arr[5] i.e. 7-2=5
print(arr[1:7:2])

#shape and reshape
a=np.array([[1,2,3,4],[2,3,4,5]])
print(a.shape)

#Reshaping means changing the shape of an array.
#The shape of an array is the number of elements in each dimension.
#By reshaping we can add or remove dimensions or change number of elements in each dimension.
b=np.array([1,7,8,9,4,5,6,10,2,3,11,12])
c=b.reshape(4,3)
print(c)

#flattening a multi-dimensional array to a 1-D array is by:
#reshape(-1)
for x in arr:
    print(x)

x=np.array([1,2,3])
y=np.array([4,5,6])
z=np.concatenate((x,y))
print(z)


#splitting the array into the given number
new_arr=np.array_split(b,3)
print(new_arr)

val=np.array(b==3)
print(val)

#sorting
print(np.sort(b))