import pytest

import numpy as np
from hypepy import t_test

def test_input():
    """
    Tests incorrect/unacceptable input data.
    These should raise a type error.
    """

    with pytest.raises(TypeError):
        t_test( data = 'some string' )

    with pytest.raises(TypeError):
        t_test( data = False )

    with pytest.raises(TypeError):
        t_test( data = 2 )

    with pytest.raises(TypeError):
        t_test( data = np.array([0, np.nan, 2]) )


def test_data():
    """
    Tests inputs data which are uninterpretable.
    These should raise a value error.
    """

    empty_array = np.array([])

    with pytest.raises(ValueError):
        t_test( data = empty_array )


def test_math():
    """
    Tests if the math being done is correct.
    """

    # Test data and expected output.
    data = np.array([1, 4, 2, 4])
    tstat_expected = 3.6666666666666661

    # Tolerance for equivalent floats
    tol = 1e-14

    tstat_computed = t_test( data = data )
    assert abs( tstat_computed - tstat_expected) < tol
