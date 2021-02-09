import time

class Node:
    def __init__(self, tag):
        self.id = tag 
        self.neighbours= []
        self.isLeaf = True
        self.isRoot = False
        self.degree = 0
        self.visited = False
        self.distanceFromRoot = 0 
    
    def addNeighbours(self, node):
        self.neighbours.append(node)
        self.degree += 1

class Graph:
    def __init__(self): 
        self.totalNodes = 0
        self.allNodes = []
        self.leaves = []
        self.degreeMoreThan2 = 0
    

def solver(fpath):
    with open(fpath, 'r', encoding='utf-8') as f:
        global nodes
        nodes = []
        roots = []
        totalRegular = 0
        data = list(map(str.strip, f.readlines()))
        totalNodes, totalEdges = data[0].split()
        totalNodes, totalEdges = int(totalNodes), int(totalEdges)
        for i in range(totalNodes):
            nodes.append(Node(i))
        for edge in data[1:]:
            # print(edge)
            node1, node2 = edge.split()
            node1, node2 = int(node1), int(node2)
            nodes[node1].addNeighbours(node2)
            nodes[node2].addNeighbours(node1)
            if nodes[node1].degree > 1: 
                nodes[node1].isLeaf = False
            if nodes[node1].degree > 2:
                # if nodes[node1] not in roots:
                    # roots.append(nodes[node1])
                nodes[node1].isRoot = True
            if nodes[node2].degree > 1:
                nodes[node2].isLeaf = False
            if nodes[node2].degree > 2:
                # roots.append(nodes[node2])
                nodes[node2].isRoot = True
        for root in nodes:
            if root.isRoot:
                # print('---new graph----')
                # print('current root ', root.id)
                if DFS(root):
                    # print('this graph is regular')
                    totalRegular += 1
                # else:
                    # print('this is not regular')
        return totalRegular


def DFS(node):        
    stack = []
    stack.append(node)
    node.visited = True
    leafDist = None
    while  len(stack) != 0:
        currNode = stack.pop()
        # currNode = nodes[nodeID]
        # print(currNode.id, end = " ") 
        for neigh in currNode.neighbours:
            if not nodes[neigh].visited:
                stack.append(nodes[neigh])
                nodes[neigh].visited = True
                nodes[neigh].distanceFromRoot = currNode.distanceFromRoot + 1 
                if nodes[neigh].isLeaf:
                    if leafDist == None:
                        leafDist = nodes[neigh].distanceFromRoot
                    else:
                        if nodes[neigh].distanceFromRoot != leafDist:
                            return False
    return True

def driver():
    for i in range(1, 11):
        inFile = "alg\stars regular\datapub\pub" + \
        f"{i:02d}" + '.in'
        outFile = "alg\stars regular\datapub\pub" + \
        f"{i:02d}" + '.out'
        t1 = time.time()
        myAns = solver(inFile)
        t2 = time.time()
        with open(outFile, 'r', encoding='utf-8') as out:
            ans = out.readlines()
            ans = list(map(str.strip, ans))
            ans = int(ans[0])
        print(myAns, '||', ans, '||', myAns == ans, 'time taken = ', t2 - t1)

if __name__ == "__main__":
    driver()
    



            
            
        
        
            
            
            

