def conf_int(data):
    """
    This function takes in an array and outputs the 95% confidence interval of the population mean.

    Arguments: data: a 1D numpy array of a list of numbers. Non-numerical values result in an error.

    Returns: interval: a 2-element 1D numpy array indicating the start and end of the 95% confidence interval.
    """

    import numpy as np

    # Doing some checks on the user input
    if len(data) == 0:
        raise ValueError("Input cannot be empty")

    # Set up the parameters
    mean = np.mean(data)

    sd = np.std(data, ddof=1)

    n = len(data)

    lower = round((mean - (1.96*(sd/np.sqrt(n)))),2)

    upper = round((mean + (1.96*(sd/np.sqrt(n)))),2)

    conf = np.array([lower, upper])

    return conf
