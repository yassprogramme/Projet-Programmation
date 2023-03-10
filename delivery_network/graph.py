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
    
    def add_edge(self, node1, 
    node2, power_min, dist=1):
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
    
    def get_path_with_power(self,src,dest,power,visited=None,path=None):
        if visited is None:
            visited = set()
        if path is None:
            path = []
        path = path + [src]
        visited.add(src)
        if src == dest:
           return path
        for neighbor in self.graph[src]:
            if neighbor[0] not in visited and power>=neighbor[1]:
                new_path = self.get_path_with_power(neighbor[0], dest,power, visited,path)
                if new_path is not None:
                    return new_path
        return None

    def get_path_with_powerr(self,src,dest,power):
        pile = [(src, [src], set())]
        while pile:
            node, path, visited = pile.pop()
            visited.add(node)
            if node == dest:
                return path
            for neighbor in self.graph[node]:
                if neighbor[0] not in visited and power>=neighbor[1]:
                    pile.append((neighbor[0], path + [neighbor[0]], visited.copy()))
        return None

                                 
    def get_min_path_with_power(self, src, dest, power): #Dijkstra
        precedent = {x:None for x in self.nodes}
        dejaTraite = {x:False for x in self.nodes}
        distance =  {x:float('inf') for x in self.nodes}
        distance[src] = 0
        a_traiter = [(0, src)]
        while a_traiter:
            dist_noeud, noeud = a_traiter.pop()
            if not dejaTraite[noeud]:
                dejaTraite[noeud] = True
                for voisin in self.graph[noeud]:
                    dist_voisin = dist_noeud + voisin[2]
                    if dist_voisin < distance[voisin[0]] and power>=voisin[1]:
                        distance[voisin[0]] = dist_voisin
                        precedent[voisin[0]] = noeud
                        a_traiter.append((dist_voisin, voisin[0]))
            a_traiter.sort(reverse=True)
        chemin=[]
        k=dest
        while k!=src:
            if k==None:
                return None
            else:
                chemin.append(k)
                k=precedent[k]
        chemin.append(src)
        chemin.reverse()
        return chemin

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
        k=0
        while self.get_path_with_power(src,dest,2**k)==None:
            k+=1
        list=[i for i in range(2**k+1)]
        a = 0
        b = len(list)-1
        m = (a+b)//2
        while a < b :
            if self.get_path_with_power(src,dest,list[m])!=None:
                b=m ##On n'exclut pas m
            else:
               a=m+1
            m=(a+b)//2
        return self.get_path_with_power(src,dest,list[a]),a


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
            edge = file.readline().split()
            if len(edge) == 3:
                node1, node2, power_min = int(edge[0]),int(edge[1]),int(edge[2])
                g.add_edge(node1, node2, power_min) # will add dist=1 by default
            elif len(edge) == 4:
                node1, node2, power_min, dist = int(edge[0]),int(edge[1]),int(edge[2]),float(edge[3]) #Pour pouvoir lire 10
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
    while Arbre_minimum.nb_edges!=N-1: # Cf Q.2
        (src,dest,power,dist)=arcs[index]
        index+=1

        x=ed.find(src)
        y=ed.find(dest)
        
        if x!=y:
            Arbre_minimum.add_edge(src,dest,power,dist)

            ed.Union(x,y)
    return Arbre_minimum
    
