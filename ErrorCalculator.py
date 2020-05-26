
import numpy as np
import math
import matplotlib.pyplot as plt

class ErrorCalculator():
    def __init__(self, y_test, Y_predict):
        self.y_test = y_test
        self.Y_predict = Y_predict
    
    def get_residuals(self):
        return self.y_test - self.Y_predict
    
    def get_standardised_residuals(self):
        return self.get_residuals() / self.get_residuals().std()
    
    def get_mse(self):
        return np.square(np.subtract(self.y_test, self.Y_predict)).mean()
    
    def get_rmse(self):
        return np.sqrt(((self.Y_predict - self.y_test) ** 2).mean())
    
    def error_summary(self):
        return pd.DataFrame({"Standardised Residuals Average Mean" : [self.get_standardised_residuals().mean()],
                             "Standardised Residuals Average Min": [self.get_standardised_residuals().min()],
                             "Standardised Residuals Average Max": [self.get_standardised_residuals().max()],
                             "MSE": [self.get_mse()],
                             "RMSE": [self.get_rmse()]},
                             columns= ["Standardised Residuals Average Mean",
                                     "Standardised Residuals Average Min",
                                     "Standardised Residuals Average Max",
                                     "MSE",
                                     "RMSE"])