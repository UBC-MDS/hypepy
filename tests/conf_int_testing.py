import numpy as np
import pytest

def conf_int(data):
    '''
    This function takes in an array and outputs the 95% confidence interval of the population mean.

    Arguments: data: a 1D numpy array of a list of numbers. Non-numerical values result in an error.

    Returns: interval: a 2-element 1D numpy array indicating the start and end of the 95% confidence interval.
    '''
#1. input is a string   - typeError
#2. input a boolean
#3. input empty list
#4. input sd as 0
#5. input has missing values
def type_test()
