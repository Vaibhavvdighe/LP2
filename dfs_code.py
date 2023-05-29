graph={
    'A':['B','C'],
    'B':['D','E'],
    'C':['G'],
    'D':[],
    'E':['F'],
    'F':[],
    'G':[]
}

visited=set()

def dfs(visited,graph,node):
    if node not in visited:
        print(node,end=" ")
        visited.add(node)
        for n in graph[node]:
            dfs(visited,graph,n)
# call function
dfs(visited,graph,'A')
print()

visitednode=[]
queue=[]
def bfs(visitednode,queue,node):
    visitednode.append(node)
    queue.append(node)
    while queue:
        m=queue.pop(0)
        print(m,end=' ')

        for neighbour in graph[m]:
            if neighbour not in visitednode:
                visitednode.append(neighbour)
                queue.append(neighbour)
bfs(visitednode,queue,'A')
