from _PointClass import Point
import numpy as np


def getDataSet(path: str):
    nodes = np.array([], float, copy=True)

    with open(f'{path}') as f:
        for line in f:
            pair = line.replace('\n', '').split(' ')
            nodes = np.append(
                nodes, [Point(float(pair[0]), float(pair[1]))])
    return nodes
