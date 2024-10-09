__name__="Dense"
from ..activations import relu,tanh,sigmoid
import numpy as np
class DenseLayer:
    def __init__(self,n_neurons,input_size,activation):
        self.input_size=input_size
        self.activation=activation
        self.n_neurons=n_neurons
        rng=np.random.default_rng(seed=42) #create a random number generator and set the initial state so the results can be replicated
        self.weights=rng.random(size=(n_neurons,input_size))
        print("weights",self.weights)
        self.bias=rng.random()
    def forward(self,X):
        activate=np.vectorize(pyfunc=self.activation)
        print(X*self.weights+self.bias)
        print(activate(X*self.weights+self.bias))
        return activate(X*self.weights+self.bias)
    
x=np.array([[-1,0,3],[-1,0,1]])

Dense=DenseLayer(n_neurons=2,input_size=3,activation=relu)
Dense.forward(x)
    
print("__package__ is",__package__)