import numpy as np
import math
import matplotlib.pyplot as plt

class Plotter():
    def __init__(self,y_test,ypred):
        self.y_test = y_test
        self.ypred = ypred
    
    def run_calculations(self):
        return self.y_test - self.ypred
    
    def plot(self):
        plt.hist(self.y_test - self.ypred)
        plt.title('Residuals Plot for predictions')
        plt.xlabel('Residuals')
        plt.ylabel('Frequency')
        return plt.show()