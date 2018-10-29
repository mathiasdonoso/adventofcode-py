from manhattan_distance import ManhattanDistance
from spiral_memory import SpiralMemory


def main():
    with open('input.txt', 'r') as input_file:
        target = input_file.read()
        algorithm = ManhattanDistance()
        spiral_memory = SpiralMemory(target, algorithm)
        result = spiral_memory.process()
        print(result)


if __name__ == "__main__":
    main()
