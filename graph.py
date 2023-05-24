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

        with open(input_file, 'r') as file:
            for row in file:
                line = row.split(':')[0]
                print(line)
                
                print(row.split(':')[1])
