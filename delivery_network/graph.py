from UnionFind import UnionFind

class Graph:
    """
    A class representing graphs as adjacency lists and implementing various algorithms on the graphs. Graphs in the class are not oriented. 
    Attributes: 
    -----------
    nodes: NodeType
        A list of nodes. Nodes can be of any immutable type, e.g., integer, float, or string.
        We will usually use a list of integers 1, ..., n.
    graph: dict
        A dictionnary that contains the adjacency list of each node in the form
        graph[node] = [(neighbor1, p1, d1), (neighbor1, p1, d1), ...]
        where p1 is the minimal power on the edge (node, neighbor1) and d1 is the distance on the edge
    nb_nodes: int
        The number of nodes.
    nb_edges: int
        The number of edges. 
    """

    def __init__(self, nodes=[]):
        """
        Initializes the graph with a set of nodes, and no edges. 
        Parameters: 
        -----------
        nodes: list, optional
            A list of nodes. Default is empty.
        """
        self.nodes = nodes
        self.graph = dict([(n, []) for n in nodes])
        self.nb_nodes = len(nodes)
        self.nb_edges = 0
    

    def __str__(self):
        """Prints the graph as a list of neighbors for each node (one per line)"""
        if not self.graph:
            output = "The graph is empty"            
        else:
            output = f"The graph has {self.nb_nodes} nodes and {self.nb_edges} edges.\n"
            for source, destination in self.graph.items():
                output += f"{source}-->{destination}\n"
        return output
    
    def add_edge(self, node1, node2, power_min, dist=1):
        """
        Adds an edge to the graph. Graphs are not oriented, hence an edge is added to the adjacency list of both end nodes. 

        Parameters: 
        -----------
        node1: NodeType
            First end (node) of the edge
        node2: NodeType
            Second end (node) of the edge
        power_min: numeric (int or float)
            Minimum power on this edge
        dist: numeric (int or float), optional
            Distance between node1 and node2 on the edge. Default is 1.
        """
        if node1 not in self.graph:
            self.graph[node1] = []
            self.nb_nodes += 1
            self.nodes.append(node1)
        if node2 not in self.graph:
            self.graph[node2] = []
            self.nb_nodes += 1
            self.nodes.append(node2)

        self.graph[node1].append((node2, power_min, dist))
        self.graph[node2].append((node1, power_min, dist))
        self.nb_edges += 1
    
    def get_edges(self):
        arcs=[]
        for node1,nodes2 in self.graph.items():
            for node in nodes2:
                if ((node1,node[0],node[1],node[2]) not in arcs) and ((node[0],node1,node[1],node[2]) not in arcs):
                    arcs.append((node1,node[0],node[1],node[2]))
        return arcs  

    def get_path_with_power(self, src, dest, power):
        def arret(liste,dest):
            for item in liste:
                if item[-1]!=dest:
                    return False
            return True
        def dist_trip(l): 
            d = 0   
            for i in range(len(l)-1):
             for j in self.graph[l[i]]:
                 if j[0] == l[i+1]:
                       d += j[2]
            return d
        composantes=self.connected_components()
        for liste in composantes:
            if src in liste:
                c=liste
        if dest not in c:
            return None
        
        chemins=[[src]]
        while not arret(chemins,dest): #si chemins est vide, ça renvoit vrai
            q=[]
            for p in chemins:
                u=p[-1]
                if u==dest:
                    q.append(p)
                else:
                    for t in self.graph[u]:
                        if not (t[0] in p) and power>=t[1]:
                            v=[i for i in p]
                            v.append(t[0])
                            q.append(v)
            chemins=q
        if chemins==[]:
            return None
        else:
            for chemin in chemins[1::]:
                if dist_trip(chemin)<dist_trip(chemin_plus_court):
                    chemin_plus_court=chemin
            return chemin_plus_court

    def connected_components(self):
        composantes_connexes=[]
        visited_nodes={noeud:False for noeud in self.nodes}

        def deep_parcours(s):
            composantes=[s]
            for neighboor in self.graph[s]:
                neighboor=neighboor[0]
                if not visited_nodes[neighboor]:
                    visited_nodes[neighboor]=True
                    composantes+=deep_parcours(neighboor)
            return composantes
        
        for s in self.nodes:
            if not visited_nodes[s]:
                composantes_connexes.append(deep_parcours(s))
        return composantes_connexes
                      
            

    def connected_components_set(self):
        """
        The result should be a set of frozensets (one per component), 
        For instance, for network01.in: {frozenset({1, 2, 3}), frozenset({4, 5, 6, 7})}
        """
        return set(map(frozenset, self.connected_components()))
    
    def min_power(self, src, dest):
        """
        Should return path, min_power. 
        """
        chemin=self.get_path_with_power(src,dest,float("inf"))
        if R==None:
            return None 
        def min_power_trip(l): 
            m= 0   
            for i in range(len(l)-1):
             for j in self.graph[l[i]]:
                 if j[0] == l[i+1] and j[1]>m:
                       m= j[1]
            return m
        chemin_min_power=chemins[0]
        p=min_power_trip(chemin_min_power)
        for chemin in chemins[1::]:
            if min_power_trip(chemin)<p:
                chemin_min_power,p=chemin, min_power_trip(chemin)
        return chemin_min_power,p



def graph_from_file(filename):
    """
    Reads a text file and returns the graph as an object of the Graph class.

    The file should have the following format: 
        The first line of the file is 'n m'
        The next m lines have 'node1 node2 power_min dist' or 'node1 node2 power_min' (if dist is missing, it will be set to 1 by default)
        The nodes (node1, node2) should be named 1..n
        All values are integers.

    Parameters: 
    -----------
    filename: str
        The name of the file

    Outputs: 
    -----------
    g: Graph
        An object of the class Graph with the graph from file_name.
    """
    with open(filename, "r") as file:
        n, m = map(int, file.readline().split())
        g = Graph(range(1, n+1))
        for _ in range(m):
            edge = list(map(int, file.readline().split()))
            if len(edge) == 3:
                node1, node2, power_min = edge
                g.add_edge(node1, node2, power_min) # will add dist=1 by default
            elif len(edge) == 4:
                node1, node2, power_min, dist = edge
                g.add_edge(node1, node2, power_min, dist)
            else:
                raise Exception("Format incorrect")
    return g


def kruskal(g):
    N=g.nb_nodes
    arcs=g.get_edges()
    arcs.sort(key=lambda x : x[2])
    Arbre_minimum=Graph(g.nodes)
    ed=UnionFind(N+1)
    index=0
    A=0 #nb d'arcs 
    while A!=N-1: # Cf Q.2
        (src,dest,power,dist)=arcs[index]
        index+=1

        x=ed.find(src)
        y=ed.find(dest)
        
        if x!=y:
            Arbre_minimum.graph[src].append((dest,power,dist))
            Arbre_minimum.graph[dest].append((src,power,dist))
            A+=1
            ed.Union(x,y)
    return Arbre_minimum
    
