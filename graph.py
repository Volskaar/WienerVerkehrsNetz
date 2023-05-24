class edge:
    def __init__(self, value, line, von, nach):
        self.value = value
        self.line = line
        self.vertexA = von
        self.vertexB = nach

class vertex:
    def __init__(self, name):
        self.name = name
        self.connections = [] #array of edges

class graph:
    def __init__(self, input_file):

        self.verteces = []
        self.edges = []
        self.newRows = []
        self.strings = []

        with open(input_file, 'r') as file:
            for row in file:
                temp = row.replace(":", " ")
                self.newRows.append(temp)

            for row in self.newRows:
                self.strings.append(row.split())

        
        print(self.strings[0][0])







