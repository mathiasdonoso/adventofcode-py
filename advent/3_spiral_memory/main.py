from spiral_memory import SpiralMemory

def main():
    with open('input.txt', 'r') as input_file:
        input = input_file.read()
        spiral_memory = SpiralMemory(input)
        result = spiral_memory.process()
        print(result)

if __name__ == "__main__":
    main()