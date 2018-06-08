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