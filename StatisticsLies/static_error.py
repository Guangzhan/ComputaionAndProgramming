# -*- coding: utf-8 -*-

import random

def juneProb(numTrials):
    june48 = 0
    for trial in range(numTrials):
        june = 0
        for i in range(446):
            if random.randint([1, 12]) == 6:
                june += 1
        if june >= 48:
            june48 += 1
    jProb = june48 / float(numTrials)
    print('Probability of at least 48 births in June = ', jProb)