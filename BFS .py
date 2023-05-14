def bfs (graph , source):
    visited = set() #already visited node
    traversal = list()# BFS travrsal node
    queue = list()# queue

    #push the root node to the queue and mark it as visited
    queue.append(source)
    visited.add(source)

#loop are runing until the que is empty
    while queue:
        #pop the front node of the queue and add it to taversal
        current_node = queue.pop(0)
        traversal.append(current_node)


#acheck all the neighbour node of the current node
        for neighbour_node in graph[current_node]:

# node are alrady visited
# push them in queue and mark as visited
            if neighbour_node not in visited:
                visited.add(neighbour_node)
                queue.append(neighbour_node)

    return traversal

def main():
    graph = {
        'A': ['B', 'C', 'D'], 
        'B': ['A', 'D', 'E'], 
        'C': ['A', 'D'], 
        'D': ['B', 'C', 'A', 'E'], 
        'E': ['B', 'D']
    }

    traversal = bfs(graph, 'A')
    print(f"BFS: {traversal}")

    
if __name__=='__main__':
    main()
