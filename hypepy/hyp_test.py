def hyp_test(data, mean_0, alpha):
    """
    Prints the t-statistic, p-value and a recommendation for rejecting or accepting the null hypothesis.

    Arguments: data: a 1-dimensional array. Non-numerical values result in an error
               mean_0: the mean (as a number) of the population under the null hypothesis. Default: 0.
               alpha: set the alpha threshold.

    Returns: results: a summary in the form of a string.
    """
    import numpy as np
    import pandas as pd
    from scipy import stats

    if isinstance(data, bool):
        raise TypeError("Data can not be a Boolean.")

    if isinstance(data, str):
        raise TypeError("Data can not be a string.")

    if isinstance(mean_0, bool):
        raise TypeError("Input can not be a Boolean.")

    if isinstance(mean_0, str):
        raise TypeError("Input can not be a string.")

    if len(data) == 0:
        raise ValueError("Data must not be empty.")

    if np.isnan(data) == True:
        raise ValueError("Data must not have missing data.")

    if 0 <= alpha > 1:
        raise ValueError("Alpha value must be between 0 and 1.")

    # initialize parameters
    alpha = alpha

    data = pd.DataFrame(np.array(data))

    # calculate the degrees of freedom
    deg_of_freedom = len(data) - 1

    # calculate the test statistic
    test_stat = (np.mean(data) - mean_0) / (np.sqrt(np.var(data) /len(data)))

    # calculate the p-value
    p_val = (1 - stats.t.cdf(test_stat, df = deg_of_freedom))

    print("The test statistic is:", test_stat)
    print("The p-value is:", p_val)

    if p_val <= alpha:
        print("The p-value is below the alpha threshold, you may reject the null hypothesis.")

    else:
        print("The p-value is above the alpha threshold, you may accept the null hypothesis.")


# Source : https://towardsdatascience.com/inferential-statistics-series-t-test-using-numpy-2718f8f9bf2f
