# hypepy

# Authors

Joe Sastrillo

Siobhan McCarter

Ivan Despot

# Project Summary

The goal of this project is to create a user-friendly and intuitive **hypothesis testing** package. Hypothesis testing belongs in the *statistical inference* domain, where an individual is attempting to determine if their results are significant or not. To accomplish this, the individual must generate a **null** and **alternative** hypotheses, and perform a series of statistical tests. That individual can use our package to make their life easier when looking for the elusive "significant" result.

This project is part of the DSCI 524 Collaborative Software Development Course for the Masters of Data Science program at the University of British Columbia.

# Function Examples

* `conf_int` - Computes the confidence interval of the mean from a population.

* `hyp_test` - Returns test-statistic, p-value and a recommendation for rejecting or accepting the null hypothesis.

* `z_score` - Computes the *Z*-score which represents how away a data point is from the mean in terms of standard deviations.

# Current Environment

There are multiple packages in both Python and R that have similar functions and features as this package. For example, [Scipy](https://docs.scipy.org/doc/scipy/reference/stats.html) has an entire module that is capable of performing advanced hypothesis testing. Likewise, base R has several similar functions, and there is a wide variety of unique hypothesis testing packages available - such a [hypothesestest](https://cran.r-project.org/web/packages/hypothesestest/hypothesestest.pdf).
