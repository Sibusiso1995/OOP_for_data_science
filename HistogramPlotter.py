import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt
from Plotter import Plotter

class HistogramPlotter(Plotter):
    def __init__(self, y_test,ypred):
        Plotter.__init__(self, y_test, ypred)