import math


class SpiralMemory(object):
    def __init__(self, target, algorithm):
        self.target = int(target)
        self.distance_algorithm = algorithm

    def process(self):
        spiral = self.generate_spiral()
        # distance = self.distance_algorithm.search(spiral, self.target)
        return spiral

    def generate_spiral(self):
        array_size = int(math.ceil(math.sqrt(self.target)))
        arr = [[0] * array_size for i in range(array_size)]
        initial_index = int(math.floor(array_size/2))
        current_i = current_j = initial_index

        for i in range(1, self.target + 1):
            arr[current_i][current_j] = i
            # To do

        return arr
