from .abstract_classes import AbstractSource

class File_source(AbstractSource):
    def __init__(self, path):
        self.path = path
    # read  source
    def read(self):
        with open(self.path, 'r') as f:
            return [eval(s) for s in f.readlines()]

if __name__ == "__main__":
    f = File_source('../data/input.txt')
    print(f.read())
