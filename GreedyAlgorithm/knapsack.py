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
    item.get_value()


def build_items():
    names = ['clock', 'painting', 'radio', 'vase', 'book', 'computer']
    vals = [170, 90, 20, 50, 10, 200]
    weights = [10, 9, 4, 2, 1, 20]
    items = []
    for i in range(len(vals)):
        items.append(Item(names[i], vals[i], weights[i]))
    return items
