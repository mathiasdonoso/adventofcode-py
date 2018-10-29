from passphrase import PassPhrase


def main():
    count = 0
    with open('input.txt', 'r') as input_file:
        read_lines = input_file.readlines()
        phrases = [line.rstrip('\n') for line in read_lines]

        for phrase in phrases:
            pass_phrase = PassPhrase(phrase)
            if pass_phrase.is_valid():
                count += 1

    print(count)


if __name__ == "__main__":
    main()
