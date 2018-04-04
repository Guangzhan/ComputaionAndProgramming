# *-* coding: utf-8 *-*


import pylab as pb

def plotHousing(impression):
    f = open('midWestHousingPrices.txt', 'r')
    labels, prices = ([], [])
    for line in f:
        year, quarter, price = line.split()
        label = year[2:4] + '\n Q' + quarter[1]
        labels.append(label)
        prices.append(float(price) / 1000)
    quarter = pb.arange(len(labels))
    