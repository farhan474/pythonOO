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
        "creates a starting number and a counter"
        self.start = start
        self.count = start

    def generate(self):
        "prints out the number and increase the count by one"
        num = self.count
        self.count = self.count+1
        return num
    
    def reset(self):
        "resets the counter to starting number"
        self.count = self.start