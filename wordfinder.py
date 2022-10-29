from random import choice


class WordFinder:
    """Word Finder: finds random words from a dictionary."""

    def __init__(self, filepath):
        self.filepath = filepath
        self.words = []
        self.readfile(self.process_line)

    def readfile(self, process_function):
        """Read the file, append each word read to the words list, and
        return the number of words read"""
        num_words = 0

        f = open(self.filepath, 'r')

        for line in f:
            word = process_function(line)
            if word:
                self.words.append(word)
                num_words += 1

        f.close()

        print(f'{num_words} words read')

    def process_line(self, line):
        """Read one line and return just the word/text without extra characters"""
        return line.strip()

    def random(self):
        """Return a random word from the list of words"""
        return choice(self.words)

