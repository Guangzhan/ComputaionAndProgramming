# -*- coding:utf-8 -*-

"""
    solve Fibnacci sequence
"""


def fib(num):
    """

    :param num: num is non-negative
    :return: Fibnacci
    """
    if num == 0 or num == 1:
        return 1
    else:
        return fib(num - 1) + fib(num - 2)


# calculate fibnacci sequence with dynamic programing
def fib_dp(num):
    fib = {}
    for k in range(num + 1):
        if k <= 2:
            fib[k] = 1
        else:
            f = fib[k - 1] + fib[k - 2]
            fib[k] = f
    return fib


# use memo to solve fibnacci
def fast_fib(num, memo={}):
    if num == 0 or num == 1:
        return 1
    try:
        return memo[num]
    except KeyError:
        result = fast_fib(num - 1, memo) + fast_fib(num - 2, memo)
        memo[num] = result
        return result


def small_test():
    n = 100
    result = fast_fib(n)
    print(result)

if __name__ == '__main__':
    small_test()