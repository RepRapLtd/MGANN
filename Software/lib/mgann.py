import math as maths
import random

class Node:
    def __init__(self, identity, neighbours):
        self.firing = False
        self.sum = 0.0
        self.neighbours = []
        for n in neighbours:
            self.neighbours.append(n)
        self.visited = False
        self.identity = identity

    def __str__(self):
        s = "node " + str(self.identity) + " : "
        for n in self.neighbours:
            s += "n: " + str(n[0])
            s += " w: " + str(n[1]) + " "
        return s

    def Output(self):
        s = str(self.identity) + " "
        for n in self.neighbours:
            s += str(n[0]) + " "
            s += str(n[1]) + " "
        return s

    def SetRandomWeights(self):
        for n in self.neighbours:
            n[1] = random.uniform(-1.0, 1.0)



class MGANN:
    def __init__(self, mgannFile):
        self.nodes = []
        count = 0
        mFile = open(mgannFile, "r")
        mLines = mFile.readlines()
        for mLine in mLines:
            count += 1
            mLine = mLine.split()
            if len(mLine) < 7:
                return
            identity = int(mLine[0])
            if identity != count:
                print("Reading file " + mgannFile + " - error at line " + str(count))
            nodes = []
            for n in range(1, 7, 2):
                nodes.append([int(mLine[n]), float(mLine[n+1])])
            self.nodes.append(Node(identity, nodes))

    def __str__(self):
        s = ""
        for n in self.nodes:
            s += str(n) + "\n"
        return s

    def SetRandomWeights(self):
        for n in self.nodes:
            n.SetRandomWeights()

    def Save(self, mgannFile):
        mFile = open(mgannFile, "w")
        for n in self.nodes:
            mFile.write(n.Output() + "\n")

m = MGANN("petersen.mgann")
m.SetRandomWeights()
print(str(m))
m.Save("tf.mgann")
