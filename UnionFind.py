class UnionFind:
    dataMap = {}
    class Node():
        def __init__(self,data):
            self.data = data
            self.rank = 0
            self.parent = None
    def makeSet(self,data):
        node = self.Node(data)
        node.parent = node
        self.dataMap[data] = node
    
    def findSet(self,node):
        parent = node.parent
        if(parent == node):
            return node
        node.parent = self.findSet(node.parent)
        return node.parent
    
    def union(self,data1,data2):
        node1 = self.dataMap[data1]
        node2 = self.dataMap[data2]
        parent1 = self.findSet(node1)
        parent2 = self.findSet(node2)
        if (parent1 == parent2):
            return
        elif(parent1.rank >= parent2.rank):
            parent1.rank = parent1.rank+parent2.rank if parent1.rank == parent2.rank else parent1.rank
            parent2.parent = parent1
        else:
            parent1.parent = parent2