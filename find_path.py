import graph.py
import path.py
import sys

#take in text file (data and subtree) upon calling command
start = None
end = None

for i in range(1, len(sys.argv)):
    start = sys.argv[1]
    end = sys.argv[2]

#open and use text file with stations
stationList = []
with open('WienerVerkehrsnetz.txt', 'r') as file:
    for line in file:
        stationList.append(line)

#create network object from graph class in graph.py
network = graph.graph(stationList)

#find and store most efficient path in path object from path.py
bestPath = network.findBestPath(start, end)

#print information to optimal path
bestPath.printPath()

#python find_path.py start ziel