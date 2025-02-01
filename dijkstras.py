import networkx as nx
import math

G = nx.Graph()

G.add_nodes_from(['S','A','B','C','D','E','F'])
G.add_edges_from([('S', 'A', {"weight": 3}), \
                  ('S', 'C', {"weight": 2}), \
                  ('S', 'F', {"weight": 6}), \
                  ('A', 'B', {"weight": 6}), \
                  ('A', 'D', {"weight": 1}), \
                  ('B', 'E', {"weight": 1}), \
                  ('C', 'A', {"weight": 2}), \
                  ('C', 'D', {"weight": 3}), \
                  ('D', 'E', {"weight": 4}), \
                  ('F', 'E', {"weight": 2})])

s_node = 'S'

Q = []
S = set(G.nodes)
D = {v: math.inf for v in G.nodes}
D[s_node] = 0

def greedy(D):
    temp = ['',math.inf]
    for x,y in D.items():
        if y < temp[1] and x in S:
            temp = [x,y]
    return temp[0]

while len(S) != 0:
    v = greedy(D)
    S.remove(v)
    Q.append(v)
    for i in list(G.neighbors(v)):
        if i not in Q:
            if D[v] + G[v][i]["weight"] < D[i]:
                D[i] = D[v] + G[v][i]["weight"]
print(D)
