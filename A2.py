
import sys
import queue

fullDomain = [1,2,3,4,5,6,7,8,9]

class cell:
    def init(self, row, col, value):
        self.row = row
        self.col = col
        self.value = value

class CSP:
    def __init__(self, inp):
        self.variables = [r + c for r in 'ABCDEFGHI' for c in '123456789']
        self.values = [int(val) for val in inp]
        self.domain = [(var, fullDomain if self.values[self.variables.index(var)] == 0 else self.values[self.variables.index(var)]) for var in self.variables]
        a = [self.colNeighbors(self.domain, i) for i in range(9)]
        #print("A IS:~")
        #print(a)
        #print("----------")
        b = [self.rowNeighbors(self.domain, i) for i in range(9)]
        c = [self.cellNeighbors(self.domain, i, j) for i in range(9) for j in range(9)]


        self.allNeighbors = (a + b + c)

        self.keys = dict((s, [u for u in self.allNeighbors if s in u]) for s in self.variables)
        self.neighbors = dict((s, set(sum(self.keys[s], [])) - set([s])) for s in self.variables)
        #self.constraints = dict((variable, neighbor) for variable in self.variables for neighbor in self.neighbors[variable])
        self.constraints = {(variable, peer) for variable in self.variables for peer in self.neighbors[variable]}
        
        

    def colNeighbors(self, b, col):
        neighbors = []
        for i in range(col, len(b), 9):
            neighbors.append(b[i])

        return neighbors

    def rowNeighbors(self, b, row):
        neighbors = []
        end = (row + 1) * 9
        start = end - 9
        for i in range(start, end, 1):
            neighbors.append(b[i])

        return neighbors
    def cellNeighbors(self, b, row, col):
        # print("R:", row, "C:", col)
        neighbors = []
        domRow = row - row % 3
        domCol = col - col % 3
        for j in range(3):
            for i in range(3):
                    neighbors.append(b[(j+domCol) + (i+domRow)*9])
        return neighbors

def fillQueue(csp):
    q = queue.Queue()
    for arc in csp.constraints:
        q.put(arc)
    return q
def getNeighbors(csp,Xi,Xj):
    return(csp.neighbours[Xi] - set(Xj))

def AC3_A_BITCH(csp):
    q = fillQueue(csp)
    '''
    while not q.empty():
        x = q.get()
        print(x)
    '''
    #GET ARCS -  call the function boi///done above
        
    #GET NEIGHBORS - call function
    while not q.empty():
        (Xi, Xj) = q.get()
        if(revision(csp,Xi,Xj)):
            if(len(csp.values[Xi]) == 0):
                return False
            for Xk in getNeighbors(csp,Xi,Xj):  #<-- do the function thing
                q.put((Xk, Xi))
    return True


def backtrack(csp):

    return bigGay


#revision algorithm. reduces domain of Xi based on constraints
def revision(csp, Xi, Xj):
    i = 0
    DOMi = set(csp.values[Xi])
    isRevised = False
    for x in DOMi:
        valid = True
        for y in csp.values[Xj]:
            if x != y:
                valid = False
        if valid:
            DOMi.pop(i)
            isRevised = True
        else:
            i += 1
    return isRevised


def printAHoe(csp):
    for x in range(81):
        if (x%9 == 0):
            print()
            print(csp.values[x],end='')
        else:
            print(csp.values[x],end='')


file = open("nickisdumb.txt", 'r')
inp = file.read()

if(len(inp) == 81):
    #call init CSP function
    print("INP:", inp)
    #print("made it here")
    lool = '003020600900305001001806400008102900700000008006708200002609500800203009005010300'
    csp_lool = CSP(lool)
    print("\nBefore AC3")
    printAHoe(csp_lool)
    finished = AC3_A_BITCH(csp_lool)
    #print(finished)
    #USED FOR CHECKING THE BOARD
    print("\n\nAfter AC3")
    printAHoe(csp_lool)
    
