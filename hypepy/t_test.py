import numpy as np

def t_test(data, mean_0 = 0):
    """
    Calculates a t-statistic of the data relative to a mean which may be specified.
    """

    # Checks if the input is correct
    err_msg = 'data must be a numpy array.'
    if not isinstance(data, np.ndarray):
        raise TypeError(err_msg)

    # Checks if there are any missing values
    err_msg = 'data has missing values.'
    if np.any(np.isnan(data)):
        raise TypeError(err_msg)

    # Check if the data is empty
    err_msg = 'data is empty'
    if data.shape[0]==0:
        raise ValueError(err_msg)

    # Compute statistics
    mu = np.mean(data)
    npts = data.shape[0]

    ss = np.sum( (data - mu)**2 )
    var = ss / (npts-1)

    sem = np.sqrt( var / npts)

    # t-statistic
    t = ( mu - mean_0 ) / sem

    return t
