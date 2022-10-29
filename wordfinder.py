from random import choice


class WordFinder:
    """Word Finder: finds random words from a dictionary."""

    def __init__(self, filepath):
        self.filepath = filepath
        self.words = []
        self.readfile()

    def readfile(self):
        """Read the file, append each word read to the words list, and
        return the number of words read"""
        num_words = 0

        f = open(self.filepath, 'r')

        for line in f:
            self.words.append(line.strip())
            num_words += 1

        f.close()

        print(f'{num_words} words read')

    def random(self):
        """Return a random word from the list of words"""
        return choice(self.words)

