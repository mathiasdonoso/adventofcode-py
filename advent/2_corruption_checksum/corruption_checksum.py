class CorruptionChecksum(object):
    def __init__(self, input):
        self.input = self.transform_input(input)

    @staticmethod
    def transform_input(input):
        new_input = []
        files = input.split('\n')
        
        for file in files:
            groups = file.split('\t')
            new_input.append(groups)
        return new_input

    def process(self):
        sum = 0
        for file in self.input:
            file = [ int(x) for x in file ]
            sum = sum + (max(file) - min(file))
        return sum
