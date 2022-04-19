import rhino3dm as rg
import networkx as nx

def createGridGraph():

    Kite = nx.path_graph(10)
    Kite.add_nodes_from([10,11])
    Kite.add_edges_from([(9,10), (10,7), (9,11), (11,7)])
    return Kite


def getNodes(Kite):

    lay =  nx.kamada_kawai_layout(Kite)

    nodes = []
    for d in lay.values():
        pt = rg.Point3d( d[0], d[1] , 0)
        nodes.append(pt)

    return nodes

def getEdges(G):

    lay =  nx.kamada_kawai_layout(G)

    edges = []
    for e in G.edges:
        p1 = rg.Point3d( lay[e[0]][0], lay[e[0]][1], 0 )
        p2 = rg.Point3d( lay[e[1]][0], lay[e[1]][1], 0 )
        line = rg.LineCurve(p1, p2)
        edges.append(line)

    return edges


"""
G = createGridGraph(3,3)
GW = addRandomWeigrhs(G)

nodes = getNodes(G)
edges = getEdges(G)
"""

