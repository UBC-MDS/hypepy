import numpy as np
import pytest
import hypepy

def hyp_test(data, mean_0):
'''
This function prints the p-value and a recommendation for
rejecting or accepting the null hypothesis.

Arguments: data: a 1-dimensional numpy array. Non-numerical values result in an error
         mean_0: the mean (as a number) of the population under the null hypothesis. Default: 0.

Returns: results: a summary in the form of a string.
'''

def hyp_test_integer(hyp_test):
'''
Test if the input data is numeric, not a string or boolean.
'''
    with pytest.raises(TypeError):
        hyp_test("my data")
        hyp_test(True)

def hyp_test_missing(hyp_test):
'''
Test if the input contains missing values.
'''
    assert data == np.isnan(data)

def hyp_test_non_zero(hyp_test):
'''
Test that the length of the data is greater than 0.
'''
    assert len(hyp_test) > 0
