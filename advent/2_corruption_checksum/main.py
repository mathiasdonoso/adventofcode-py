from corruption_checksum import CorruptionChecksum


def main():
    with open('input.txt', 'r') as input_file:
        input = input_file.read()
        corruption_checksum = CorruptionChecksum(input)
        result = corruption_checksum.process()
        print(result)


if __name__ == "__main__":
    main()
