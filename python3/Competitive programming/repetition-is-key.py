from collections import defaultdict


class fileSystem:
    def __init__(self):
        self.paths = defaultdict()

    def createPath(self, path, value):
        if len(path) == 0  or path == "/" or path in self.paths:
            return False

        parent = '/'.join(path.split('/')[:-1])
        if parent not in self.paths and len(parent)

        self.paths[path] = value
        return True