'''
V = visit 
T = traversal
Q = queue
G = graph
S = sourch


'''

def BreathFirstSearch(G,S):
    V= set()#travers the node
    T =list()# bfs traversal node
    Q = list()#queue

    Q.append(S)
    V.add(S)


    while Q:
        node = Q.pop(0)
        T .append(node)

        for neighber_node in G[node]:

            if neighber_node not in V:
                V.add(neighber_node) 
                Q.append(neighber_node)

    return T

def main():

    G = {
        'A' :['B','C','D'],
        'B' :['A','D','E'],
        'C':['A','D'],
        'D':['B','C','A','E'],
        'E' :['B','D']
    }

    T = BreathFirstSearch(G , 'A')
    print(f"BFS:{T}")


    if __name__=="__main__":
        main()
