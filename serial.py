"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start):
        """Create a new SerialGenerator object and initialize starting value"""
        self.start = start
        self.num = start
        self.incr = 0

    def generate(self):
        """Return the next sequential number"""
        self.num = self.start + self.incr
        self.incr += 1
        return self.num

    def reset(self):
        """Reset the number back to the original start number"""
        self.num = self.start
        self.incr = 0
