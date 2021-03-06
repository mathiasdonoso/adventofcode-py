from inverse_captcha import InverseCaptcha


def main():
    with open('input.txt', 'r') as input_file:
        input = input_file.read()
        captcha = InverseCaptcha(input)
        result = captcha.process()

        print(result)


if __name__ == "__main__":
    main()