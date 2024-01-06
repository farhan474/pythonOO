"""Word Finder: finds random words from a dictionary."""
from random import choice

class WordFinder:    
    def __init__(self, file_path):
        self.file = open(file_path, r)
        self.lines = self.file.readlines()
    
    def random(self):
        return choice(self.lines)
    

class SpecailWordFinder(WordFinder):
    def __init__(self, file_path):
        super().__init__(file_path)
    
    def random():
        filtered_lines = [line.strip() for line in self.lines if line.strip() and not line.startswith('#')]
        return choice(filtered_lines)