class PassPhrase(object):
    def __init__(self, phrase):
        self.phrase = phrase

    def is_valid(self):
        valid = True
        phrase = self.phrase.split()
        for word in phrase:
            count = self.phrase.count(word)
            if count > 1:
                valid = False

        return valid
