import numpy as np
import math
import matplotlib.pyplot as plt
from Plotter import Plotter
import pandas as pd

class ScatterPlotter(Plotter):
    def __init__(self, y_test, ypred):
        Plotter.__init__(self, y_test, ypred)

    def plot(self):
        chart = pd.DataFrame({"y_test": self.y_test, "y_prediction": self.ypred})
        chart.plot.scatter(x="y_test", y="y_prediction", c="DarkBlue")
        plt.title("Prediction vs Actual values")
        plt.xlabel("Actual")
        plt.ylabel("Prediction")
        return plt.show()