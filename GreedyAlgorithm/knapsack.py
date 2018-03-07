# -*- coding:utf-8 -*-

"""
    Knapsack problem solving with Greedy algorithm
"""


class Item(object):
    def __init__(self, n, v, w):
        self.name = n
        self.value = v
        self.weight = w

    def get_name(self):
        return self.name

    def get_value(self):
        return self.value

    def get_weight(self):
        return self.weight

    def __str__(self):
        result = '<' + self.name + ', ' + str(self.value) \
            + ', ' + self.weight + '>'
        return result


def value(item):
    return item.get_value()


def weight_inverse(item):
    return 1.0 / item.get_value


def density(item):
    return item.get_value / item.get_weight()


def greedy(items, max_weight, key_function):
    """

    :param items:
    :param max_weight:
    :param key_function:
    :return:
    """

    items_copy = sorted(items, key=key_function, reverse=True)
    result = []
    total_value = 0
    total_weight = 0
    for i in range(len(items_copy)):
        if(total_weight + items_copy[i].get_weight()) <= max_weight:
            result.append(items_copy[i])
            total_weight += items_copy[i].get_weight()
            total_value += items_copy[i].get_value()
    return result, total_value


def build_items():
    names = ['clock', 'painting', 'radio', 'vase', 'book', 'computer']
    vals = [170, 90, 20, 50, 10, 200]
    weights = [10, 9, 4, 2, 1, 20]
    items = []
    for i in range(len(vals)):
        items.append(Item(names[i], vals[i], weights[i]))
    return items
