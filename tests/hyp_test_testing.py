import numpy as np
import pytest
from hypepy import hyp_test


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
