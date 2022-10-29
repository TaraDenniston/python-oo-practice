from wordfinder import WordFinder

class SpecialWordFinder(WordFinder):
    """
    A Random Word Finder that works with files that include blank lines and 
    comments. 
    """

    def process_line(self, line):
        """Read one line and return just the word/text without extra characters.
        Ignore blank lines or lines beginning with '#'"""
        if line[0] != '#' and line[0] != '':
            return line.strip()
