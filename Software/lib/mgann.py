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
        s = ""
        if self.identity < 10:
            s += " "
        if self.identity < 100:
            s += " "
        s += "node " + str(self.identity) + " : "
        if self.sum >= 0.0:
            s += " "
        s += "{:.6f}".format(self.sum)
        if self.firing:
            s += " F "
        else:
            s += "   "
        for n in self.neighbours:
            s += "n: " + str(n[0])
            s += " w: "
            if n[1] >= 0:
                s += " "
            s += "{:.6f}".format(n[1]) + ", "
        return s

    def Save(self):
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
            count += 1

    def Step(self):
        for n in self.nodes:
            n.sum = 0.0
        for n in self.nodes:
            if n.firing:
                for ngh in n.neighbours:
                    self.nodes[ngh[0]].sum += ngh[1]
        for n in self.nodes:
            n.firing = n.sum > 0

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
            mFile.write(n.Save() + "\n")

m = MGANN("30-node-8-girth.mgann")
m.SetRandomWeights()
m.nodes[4].firing = True
m.nodes[10].firing = True
m.nodes[11].firing = True
m.nodes[23].firing = True
print(str(m))
for s in range(8):
    m.Step()
print(str(m))
m.Save("tf.mgann")
