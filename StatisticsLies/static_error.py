# -*- coding: utf-8 -*-

import random

def juneProb(numTrials):
    june48 = 0
    for trial in range(numTrials):
        june = 0
        for i in range(446):
            if random.randint(1, 12) == 6:
                june += 1
        if june >= 48:
            june48 += 1
    jProb = june48 / float(numTrials)
    print('Probability of at least 48 births in June = ', jProb)


def anyProb(numTrials):
    anyMonth48 = 0
    for trial in range(numTrials):
        months = [0] * 12
        for i in range(446):
            months[random.randint(0, 11)] += 1
        if max(months) >= 48:
            anyMonth48 += 1
    aProb = anyMonth48 / float(numTrials)
    print('Probability of at least 48 births in June = ', aProb)


def main():
    juneProb(100)

if __name__ == '__main__':
    main()