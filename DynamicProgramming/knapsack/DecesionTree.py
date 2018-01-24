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
        return result


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
        with_val, with_to_take = max_val(to_consider[1:],
                                         avail - next_item.get_weight())
        with_val += next_item.get_weight()
        with_out_val, with_out_to_take = max(to_consider[1:], avail)

        # Choose better branch
        if with_val > with_out_val:
            result = (with_out_val, with_out_to_take)

    return result




def small_test():
    names = ['a', 'b', 'c', 'd']
    vals = [6, 7, 8, 9]
    weights = [3, 3, 2, 5]
    items = []
    for i in range(len(vals)):
        items.append(items(names[i], vals[i], weights[i]))
    val, taken = max_val(items, 5)
    for item in taken:
        print(item)
    print('Total value of items taken =', val)


if __name__ == '__main__':
    small_test()
