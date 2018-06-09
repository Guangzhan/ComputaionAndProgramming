# -*- coding:utf-8 -*-

import matplotlib.pylab as pylab

def get_data(file_name):
    data_file = open(file_name, 'r')
    distances = []
    masses = []
    for line in data_file:
        d, m = line.split()
        distances.append(float(m))
        masses.append(float(m))
    data_file.close()
    return masses, distances


def plot_data(input):
    masses, distances = get_data(input)
    masses = pylab.array(masses)
    distances = pylab.array(distances)

    forces = masses * 9.81
    pylab.plot(forces, distances, 'bo', label='Measured displacements')
    pylab.xlabel('|Force|(Newtons)')
    pylab.ylabel('Distance(meters')

def fit_data(input):
    masses, distances = get_data(input)
    masses = pylab.array(masses)
    distances = pylab.array(distances)

    forces = masses * 9.81
    pylab.plot(forces, distances, 'bo', label='Measured displacements')
    pylab.xlabel('|Force|(Newtons)')
    pylab.ylabel('Distance(meters')

    a, b = pylab.polyfit(forces, distances, 1)
    predict_distances = a * pylab.array(forces) + b
    k = 1.0 / a
    pylab.plot(forces, predict_distances, label='Displacement pridicted by \nlinear fit k=' + str(round(k, 5)))
    pylab.legend(loc='best')









