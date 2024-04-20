class FileSystem:
    def __init__(self):
        self.paths = {}

    def createPath(self, path, value):

        if path == "/" or len(path) == 0 or path in self.paths:
            return False

        parent = path[:path.rfind("/")]
        if len(parent) > 1 and path not in self.paths:
            return False

        self.paths[path] = value
        return True

    def get(self, path):
        return self.paths.get(path, -1)


if __name__ == "__main__":
    fS = FileSystem()
    print(fS.createPath("/leet", 1))
    print(fS.get("/leet"))
    print(fS.createPath("/leet/code", 2))
    print(fS.get("/c"))
