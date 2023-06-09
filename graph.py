import re
import sys

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
        self.visited = False
        self.distance = sys.maxsize
        self.previous = None

class Graph:
    def __init__(self, input_file):
        self.inputFile = input_file
        self.verteces = []
        self.edges = []
        self.line = []

    #~~~~~~~~~~~~~~~~~~~~~ Create edges based on input ~~~~~~~~~~~~~~~~~~~~~
    def defineEdges(self):
        #1. iterate through data file and seperate informations
        newRows = []

        with open(self.inputFile, 'r') as file:
            for row in file:
                #Löscht den ":" vor den Liniennamen
                temp = row.replace(":", " ")
                #Löst die Stationen und Wertigkeiten aus dem Text raus und erstellt ein 2d arry
                matches = re.findall(r'(?:U\d+|"[^"]*"|\d*[A-Za-z]|[A-Za-z]|\d+)', temp)
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
                    line = newRows[i][0]

                #get to
                elif counter == 0:
                    von = newRows[i][j].replace('"', '')
                    counter += 1

                #get weight
                elif counter == 1:
                    value = int(newRows[i][j])
                    counter += 1

                #get from
                else:
                    nach = newRows[i][j].replace('"', '')
                    counter = 0
                    self.edges.append(Edge(value, line, von, nach))
                    j = j-1
                j += 1

        '''  
        #Test print edges
        for edge in self.edges:
            print("From: " + edge.vertexA + " To: " + edge.vertexB + " Weight: " + str(edge.value) + " On: " + edge.line)
        ''' 

    #~~~~~~~~~~~~~~~~~~~~~ Create vertices based on edges ~~~~~~~~~~~~~~~~~~~~~
    def defineVerteces(self):
        #iterate through all edges and create for each vertex on an edge a new vertex, if not yet existing
        for edge in self.edges:
            vertexExists = False
            for vertex in self.verteces:
                if edge.vertexA == vertex.name:
                    vertexExists = True
            
            if vertexExists == False:
                self.verteces.append(Vertex(edge.vertexA))  
            
        for edge in self.edges:
            vertexExists = False
            for vertex in self.verteces:
                if edge.vertexB == vertex.name:
                    vertexExists = True
            
            if vertexExists == False:
                self.verteces.append(Vertex(edge.vertexB)) 

        for vertex in self.verteces:
            for edge in self.edges:
                if edge.vertexA == vertex.name or edge.vertexB == vertex.name:
                    vertex.connections.append(edge)

        '''
        #Test print edges
        for vertex in self.verteces:
            for connection in vertex.connections:
                if vertex.name == connection.vertexA:
                    print("Station: " + vertex.name + " connected to: " + connection.vertexB)
                if vertex.name == connection.vertexB:
                    print("Station: " + vertex.name + " connected to: " + connection.vertexA)
        ''' 

    def get_vertex(self, name):
        for vertex in self.verteces:
            if vertex.name == name:
                return vertex
        return None
 
    #~~~~~~~~~~~~~~~~~~~~~ Dijkstra shortest path algorithm ~~~~~~~~~~~~~~~~~~~~~
    def dijkstra(self, start_vertex_name, end_vertex_name):
        start_vertex = self.get_vertex(start_vertex_name)
        end_vertex = self.get_vertex(end_vertex_name)

        #error condition
        if start_vertex is None or end_vertex is None:
            print("Ungültige Station(en).")
            return

        #initialize starting distance
        start_vertex.distance = 0
        current_vertex = start_vertex

        while current_vertex is not None:
            current_vertex.visited = True

            #iterate through connection of current vertex
            for connection in current_vertex.connections:
                neighbor_vertex = None

                #checks if either A or B is the current vertex and sets the neighbor vertex
                if connection.vertexA == current_vertex.name:
                    neighbor_vertex = self.get_vertex(connection.vertexB)

                elif connection.vertexB == current_vertex.name:
                    neighbor_vertex = self.get_vertex(connection.vertexA)

                #append line to array
                self.line.append(connection.line)

                #calculate new vertex distance
                if neighbor_vertex is not None and not neighbor_vertex.visited:
                    new_distance = current_vertex.distance + connection.value

                    #compares distances and sets new node distance to total distance
                    #backtrack to previous node
                    if new_distance < neighbor_vertex.distance:
                        neighbor_vertex.distance = new_distance
                        neighbor_vertex.previous = current_vertex

            #reset variables
            next_vertex = None
            next_distance = sys.maxsize

            #iterate through verteces and set next vertex if not visited
            for vertex in self.verteces:
                if not vertex.visited and vertex.distance < next_distance:
                    next_vertex = vertex
                    next_distance = vertex.distance

            current_vertex = next_vertex

        #~~~~~~~~~~~~~~~~~~~~~ Output ~~~~~~~~~~~~~~~~~~~~~
        print("Shortest path from "+ start_vertex_name +" to " + end_vertex_name)
        print("Total distance: "+ str(end_vertex.distance))
        path = []
        vertex = end_vertex
        
        while vertex is not None:
            path.insert(0, vertex.name)
            for conn in vertex.connections:
                if vertex.previous != None:
                    if conn.vertexA == vertex.previous.name and conn.vertexB == vertex.name:
                        path.insert(0, conn.line)
            
            vertex = vertex.previous


        print(" -> ".join(path))




#python find_path.py WienerVerkehrsNetz.txt Leopoldau Museumsquartier
