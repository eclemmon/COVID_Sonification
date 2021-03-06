import numpy

def linear_to_logistic(lin_input, lin_min, lin_max, logistic_min=-1, logistic_max=1, k=1):
    """
    This function will transform a y input within a chosen linear functions y-min and -max into the the output
    of a sigmoid function based on a determined logistic functions minimum and maximum as x approaches inf and -inf.
    the logistic function's k can also be manipulated.
    :param lin_input: the input you want transformed
    :param lin_min: the minimum of your data set's values
    :param lin_max: the maximum of your data set's values
    :param logistic_min: the new minimum of the sigmoid function as x approaches -inf
    :param logistic_max: the new maximum of the sigmoid function as x approaches inf
    :param k: the slope of the sigmoid function at its midpoint
    :return: returns a y value from the sigmoid function based on the transformed lin_input
    """
    linear_range = lin_max - lin_min
    logistic_range = logistic_max - logistic_min
    logistic_linear_ratio = logistic_range / linear_range
    intercept = logistic_max - lin_max * logistic_linear_ratio
    x = lin_input * logistic_linear_ratio + intercept
    midpoint = (logistic_max+logistic_min) / 2
    result = (logistic_max-logistic_min) / (1 + numpy.exp(-k * (x - midpoint))) + logistic_min
    return result


if __name__ == "__main__":
    print("should be ~10: ", linear_to_logistic(0, 0, 10000, logistic_min=10, logistic_max=20, k=1))
    print("should be ~20: ", linear_to_logistic(10000, 0, 10000, logistic_min=10, logistic_max=20, k=1))
    print("should be 15: ", linear_to_logistic(5000, 0, 10000, logistic_min=10, logistic_max=20, k=1))
    print("should be 22: ", linear_to_logistic(15, 10, 20, logistic_min=20, logistic_max=24, k=1))
    print("should be ~24: ", linear_to_logistic(20, 10, 20, logistic_min=20, logistic_max=24, k=1))
    print("should be ~20: ", linear_to_logistic(10, 10, 20, logistic_min=20, logistic_max=24, k=1))

