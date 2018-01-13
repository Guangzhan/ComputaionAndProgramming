# -*- coding:utf-8 -*-

# The following class was defined in an earlier chapter,
# and is used here.


class Item(object):
    def __init__(self, n, v, w):
        self.name = n
        self.value = float(v)
        self.weight = float(w)

    def get_name(self):
        return self.name

    def get_value(self):
        return self.value

    def get_weight(self):
        return self.weight

    def __str__(self):
        result = '<' + self.name + ', ' + str(self.value)\
                 + ', ' + str(self.weight) + '>'


def max_val(to_consider, avail):
    """

    :param to_consider:
    :param avail:
    :return:
    """
    if to_consider == [] and avail == 0:
        result = (0, ())
    elif to_consider[0].get_weight() > avail:
        result = max_val(to_consider[1:], avail)
    else:
        next_item = to_consider[0]

    return result
