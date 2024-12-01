import numpy as np

arr = np.ones((4,4))
print("Ones \n", arr)

arr1 = np.arange(11)
print(arr1)

a = np.array([3,4,8,2,3])
b = np.array([2,2,2,2,2])
arr2 = np.array([2,3,4,5,6,4,7,2,5])
reshaped= arr2.reshape((3, 3))

print("Addition", a + b)
print("Subtraction", a - b)
print("Reshaped Array:\n", reshaped)
