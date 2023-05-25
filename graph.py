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
            line = ''
            von = ''
            nach = ''
            value = 0

            #initialize counter to keep track which station is "from" and which is "to"
            counter = 0
            j = 0

            while j < len(newRows[i]):
                #get line
                if counter == 0 and newRows[i][j] == newRows[i][0]:
                    line = newRows[i][j]
                    #print("Line: " + line)

                #get to
                elif counter == 0:
                    von = newRows[i][j]
                    #print("From: " + newRows[i][j] + " (ctr: " + str(counter) + ")")
                    counter += 1

                #get weight
                elif counter == 1:
                    value = newRows[i][j]
                    #print("Value: " + str(newRows[i][j]) + " (ctr: " + str(counter) + ")")
                    counter += 1

                #get from
                else:
                    nach = newRows[i][j]
                    #print("To: " + newRows[i][j] + " (ctr: " + str(counter) + ")")
                    counter = 0
                    self.edges.append(Edge(value, line, von, nach))
                    j = j-1
                j += 1

        #'''  
        #Test print edges
        for edge in self.edges:
            print("From: " + edge.vertexA + " To: " + edge.vertexB + " Weight: " + edge.value)
        #''' 
