class Edge:
    def __init__(self, value, line, von, nach):
        self.value = value
        self.line = line
        self.vertexA = von
        self.vertexB = nach

class Vertex:
    def __init__(self, name):
        self.name = name
        self.connections = [] #array of edges

class Graph:
    def __init__(self, input_file):
        self.inputFile = input_file
        self.verteces = []
        self.edges = []

    def setup(self):
        #1. iterate through data file and seperate informations
        newRows = []

        with open(self.inputFile, 'r') as file:
            for row in file:
                temp = row.replace(":", " ")
                newRows.append(temp.split())

        #2. iterate through information array and create verteces and edges
        for i in range(len(newRows)):
            for content in newRows[i]:
                print(newRows[i].index(content)%2)

                #get line
                if content == newRows[i][0]:
                    line = content

                #get to
                if newRows[i].index(content)%3 == 0:
                    nach = content

                #get weight
                elif newRows[i].index(content)%2 == 0:
                    value = int(content)

                #get from
                else:
                    von = content
                
                #self.edges.append(Edge(value, line, von, nach))

        #Test print edges
        for edge in self.edges:
            print("From: " + edge.von + " To: " + edge.nach + " Weight: " + edge.value)







