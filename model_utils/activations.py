import numpy as np
def relu(x):
    return np.maximum(x,0)

def softmax(input_vector):
    return input_vector.exp()/input_vector.sum()

def sigmoid(x):
    return 1/(1+np.exp(-x))

def tanh(x):
    return np.tanh(x)

