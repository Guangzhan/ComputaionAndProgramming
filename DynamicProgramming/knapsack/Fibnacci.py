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
