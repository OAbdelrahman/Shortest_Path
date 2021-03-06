# Dijkstra's shortest path greedy algorithm
# Find the min priority vertex from the list of given vertices
# Each vertex in the form of a list with priority as the first # element returns the min vertex and removes it from the list def extractMin(verts):

def extractMin(verts):
    minIndex = 0
    for v in range(1,len(verts)):
        if verts[v][1] < verts[minIndex][1]:
            minIndex = v
    return verts.pop(minIndex)


# Dijkstra's shortest path algorithm def shortest(g):
# Create a list of vertices and their current shortest distances
# from vertex 0
# [vertNum, dist] nVerts = len(g)

def shortest(g):
    nVerts = len(g)
    vertsToProcess = [[i, float("inf")] for i in range(nVerts)]

    # Start at vertex 0 - it has a current shortest distance of 0 
    vertsToProcess[0][1] = 0

    # Start with an empty list of processed edges 
    vertsProcessed = []
    
    while len(vertsToProcess) > 0:
        u = extractMin(vertsToProcess) 
        vertsProcessed.append(u)

        #print("to process:",vertsToProcess)
        #print(" processed:",vertsProcessed)
        # Examine all potential verts remaining 
        for v in vertsToProcess:

            # Only care about the ones that are adjacent to u 
            if g[u[0]][v[0]] > 0:
                # Update the distances if necessary 
                if u[1] + g[u[0]][v[0]] < v[1]:
                    v[1] = u[1] + g[u[0]][v[0]]
    print(vertsProcessed)

## There comes my method:
def mst(g):
    nVerts = len(g)
    vertsToProcess = [[i, float("inf")] for i in range(nVerts)]         ## initializing all the vertices = infinity
    vertsToProcess[0][1] = 0            ## Starting at vertix 0
    vertsProcessed = []         ## Technically the working tree (blue dots, if you will)
    mstEdges= []

    while len(vertsToProcess) != 0:
        u = extractMin(vertsToProcess)
        
        for v in vertsToProcess:
            if g[u[0]][v[0]] > 0:
                if g[u[0]][v[0]] < v[1]:
                    v[1] = g[u[0]][v[0]]
        
        vertsProcessed.append(u) 
    
    ## building the edges from the vertices in the order they were processed
    for i in vertsProcessed:
        row = g[i[0]]
        mstEdges.append( [i[0], row.index(i[1])] )

    mstEdges[0][1]= -1  
    
    print(mstEdges)



if __name__ == "__main__":
    graph = [[0, 7, 0, 0, 0, 10, 15, 0],
            [7, 0, 12, 5, 0, 0, 0, 9],
            [0, 12, 0, 6, 0, 0, 0, 0],
            [0, 5, 6, 0, 14, 8, 0, 0],
            [0, 0, 0, 14, 0, 3, 0, 0],
            [10, 0, 0, 8, 3, 0, 0, 0],
            [15, 0, 0, 0, 0, 0, 0, 0],
            [0, 9, 0, 0, 0, 0, 0, 0]]

    mst(graph)
    