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

    width = 0.8 #
    if impression == 'flat':
        pb.semilogy()

    pb.bar(quarter, prices, width)
    pb.xticks(quarter + width / 2.0, labels)
    pb.title('Housing Prices in U.S. Midwest')
    pb.xlabel('Quarter')
    pb.ylabel('Average Price ($1000\'s')
    if impression == 'flat':
        pb.ylim(10, 10**3)
    elif impression  == 'volatile':
        pb.ylim(180, 220)
    elif impression == 'fair':
        pb.ylim(150, 250)
    else:
        raise ValueError

def main():
    plotHousing('flat')
    pb.figure()
    plotHousing('volatile')
    pb.figure()
    plotHousing('fair')


if __name__ == '__main__':
    main()