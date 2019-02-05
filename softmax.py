import numpy as np 

def softmax(x):
	return np.exp(x) / np.sum(np.exp(x), axis=0)

x = [1,2,3,5]

print (softmax(x))
print ("Sum of softamx(x)", np.sum(softmax(x)))
print ("Sum is always = 1")