import numpy as np
import pytest
from hypepy import hyp_test


def test_hyp_test_integer():
    '''
    Test if the input data is numeric, not a string or boolean.
    '''
    with pytest.raises(TypeError):
        hyp_test( data = "my data", mean_0=1, alpha=0.05)

    with pytest.raises(TypeError):
        hyp_test(data = True, mean_0=1, alpha=0.05)

def test_hyp_test_missing():
    '''
    Test if the input contains missing values.
    '''
    data = np.array([0, np.nan, 2])
    with pytest.raises(ValueError):
        hyp_test(data, mean_0=1, alpha = 0.05)

def test_hyp_test_non_zero():
    '''
    Test that the length of the data is greater than 0.
    '''
    with pytest.raises(ValueError):
        data = np.array([])
        hyp_test(data, mean_0=1, alpha=0.05)
