import numpy as np
import pytest
from hypepy import conf_int


def test_type():
    '''
    This tests whether there are incompatible data types in the input array. This includes the following:
    Strings, booleans, NA values.
    This should return a typeError.
    '''
    with pytest.raises(TypeError):
        conf_int("this is a string, not an array!")
        conf_int(False)

    # Test array with NA value present
    NA_test = np.array([1, 2, 3, 4, np.nan])

    with pytest.raises(ValueError):
        conf_int(NA_test)


def test_length():
    '''
    This function tests whether the input data array is empty, and throws a ValueError if it is.
    '''

    # An empty array
    data_test = np.array([])

    with pytest.raises(ValueError):
        conf_int(data_test)

def test_math():
    '''
    This function tests whether the math/output in the conf_int function is correct.
    '''

    # This array has a mean of 3 and a sd of 1.5811388300842
    data = np.array([1,2,3,4,5])

    assert np.array_equal(conf_int(data), np.array([1.61, 4.39]))
