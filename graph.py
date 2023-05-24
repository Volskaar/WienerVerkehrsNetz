import re

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
                #Löscht den ":" vor den Liniennamen
                temp = row.replace(":", " ")
                #Löst die Stationen und Wertigkeiten aus dem Text raus und erstellt ein 2d arry
                matches = re.findall(r'(?:U\d+|\d+|"[^"]*")', temp)
                newRows.append(matches)

        #2. iterate through information array and create verteces and edges
        for i in range(len(newRows)):

            #initialize counter to keep track which station is "from" and which is "to"
            counter = 0
            for content in newRows[i]:
                print(newRows[i].index(content)%3)
                print("Test "+ content)

                #get line
                if content == newRows[i][0]:
                    line = content

                #get to
                elif newRows[i].index(content)%2 == 1 and counter != 1:
                    von = content
                    counter = 1

                #get weight
                elif newRows[i].index(content)%2 == 0:
                    value = int(content)

                #get from
                else:
                    nach = content
                    counter = 0

                
                
                #self.edges.append(Edge(value, line, von, nach))
              
        #Test print edges
        for edge in self.edges:
            print("From: " + edge.von + " To: " + edge.nach + " Weight: " + edge.value)







