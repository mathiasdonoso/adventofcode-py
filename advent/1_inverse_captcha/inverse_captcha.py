class InverseCaptcha(object):
    def __init__(self, input):
        self.input = input

    def process(self):
        sum = 0
        max_index = len(self.input) - 1
        for i, char in enumerate(self.input):
            if i < max_index:
                if char == self.input[i+1]:
                    print(char)
                    sum = sum + int(char)
                    print('suma = {}'.format(sum))
            else:
                if char == self.input[0]:
                    print(char)
                    sum = sum + int(char)
                    print('suma = {}'.format(sum))
        return sum
            