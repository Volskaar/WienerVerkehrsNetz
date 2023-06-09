import graph
import sys

#take in text file (data and subtree) upon calling command
input_file = None
start = None
end = None

for i in range(1, len(sys.argv)):
    input_file = sys.argv[1]
    start = sys.argv[2]
    end = sys.argv[3]

network = graph.Graph(input_file)
network.defineEdges()
network.defineVerteces()
network.dijkstra(start, end)

#python find_path.py WienerVerkehrsNetz.txt Leopoldau Niederhofstrasse