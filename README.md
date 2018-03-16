# hypepy

Status: [![Build Status](https://travis-ci.org/UBC-MDS/hypepy.svg?branch=master)](https://travis-ci.org/UBC-MDS/hypepy)

# Authors

Joe Sastrillo

Siobhan McCarter

Ivan Despot

# Project Summary

The goal of this project is to create a user-friendly and intuitive **hypothesis testing** package as a reimplementation of existing functions in the R stats package.

Hypothesis testing belongs in the *statistical inference* domain, where an individual is attempting to determine if their results are significant or not. To accomplish this, the individual must generate a **null** and **alternative** hypotheses, and perform a series of statistical tests. That individual can use our package to make their life easier when looking for the elusive "significant" result.

Why is this useful? We aimed to create a package in which you could easily take in a data set and determine whether to accept or reject the null. The package does not require two inputs of data sets. Instead, you can compare your data set to a mean that you choose.  

This project is part of the DSCI 524 Collaborative Software Development Course for the Masters of Data Science program at the University of British Columbia.


# Functions

* `conf_int`

  * Computes the confidence interval of the mean from a sample.
  * Arguments:
    * `data`: a 1-dimensional numpy array of a list of numbers. Non-numerical values result in an error.
  * Returns:
    *  `interval`: a 2 element 1-dimensional numpy array indicating the start and end of the 95% confidence interval.

* `hyp_test`
  * Prints the t-statistic, p-value and a recommendation for rejecting or accepting the null hypothesis.
  * Arguments:
    * `data`: a 1-dimensional numpy array. Non-numerical values result in an error.
    * `mean_0`: the mean (as a number) of the population under the null hypothesis. Default: 0.
    * `alpha`: Threshold for type I errors. Float is between 0 and 1.
  * Returns:
    * `results`: a summary text

* `t_test`
  * Calculates a t-statistic of the data relative to a mean which may be specified.
  * Arguments
    * `data`: a 1-dimensional numpy array. Non-numerical values result in an error.
    * `mean_0`: the mean (as a number) of the population under the null hypothesis. Default: 0.
  * Returns:
    * `t`: the t-statistic as a number

# Installation and Execution

To install the package, please run the following command in your console:

`pip install git+https://github.com/UBC-MDS/hypepy.git`

To run all of the tests run the following command in your console:

`python -m pytest`

# Current Environment

There are multiple packages in both Python and R that have similar functions and features as this package. For example, [Scipy](https://docs.scipy.org/doc/scipy/reference/stats.html) has an entire module that is capable of performing advanced hypothesis testing. Likewise, base R has several similar functions, and there is a wide variety of unique hypothesis testing packages available - such a [hypothesestest](https://cran.r-project.org/web/packages/hypothesestest/hypothesestest.pdf).

# Example of Use

First, we need to import the packages necessary:

```
import hypepy as hp
import numpy as np
```

Suppose we are given the heights (in inches) of the following students in a class.

```
heights = np.array([72.6, 57.2, 67.6, 64.8, 59.3, 72.0, 67.2, 61.3, 64.7, 59.6])
```

We are told that the average height of a student in the class is equal to 70 inches, the average height of all students in a school. We test the null hypothesis that the average height of the class is 70 by performing a t-test.

First, we can obtain the t-statistic for the situation where the heights are given and the mean is assumed to be 70.

```
t = hp.t_test(data = heights, mean_0 = 70)
print(t)
```

To interpret the t-statistic, we obtain the p-value, the probability of obtaining the above statistic given that (assuming that) the null hypothesis is true^[Devore, J. (n.d.). Probability and statistics for engineering and the sciences.]. If the probability is low (below the usual significance level of 5%), this means it is unlikely that the data was obtained under our null hypothesis, so we reject it. To compute the p-value and make the comparison, use

```
hp.hyp_test(data = heights, mean_0 = 70, alpha = 0.05)
```

Finally, we obtain a 95% confidence interval.

```
hp.conf_int(data = heights)
```

We see that this confidence interval does not contain the null hypothesis mean of 70. Under the null hypothesis, this would happen about 5% of the time.
