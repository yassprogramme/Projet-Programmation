from UnionFind import UnionFind
from collections import deque
import heapq
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
        self.edges=[]
        self.power=[]
    

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

    def get_path_with_power(self,src,dest,power):
        queue = deque([(src, [src])])
        visited = set([src])
        while queue:
            (node, path) = queue.popleft()
            if node == dest:
                return path
            for neighbor in self.graph[node]:
                if neighbor[0] not in visited and power>=neighbor[1]:
                    visited.add(neighbor[0])
                    queue.append((neighbor[0], path + [neighbor[0]]))
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
        def bfs(start_node, visited):
            component = []
            queue = deque([start_node])
            visited[start_node] = True
            while queue:
                node = queue.popleft()
                component.append(node)
                for neighbor in self.graph[node]:
                    if not visited[neighbor[0]]:
                        visited[neighbor[0]] = True
                        queue.append(neighbor[0])
            return component
        visited = {node:False for node in self.nodes}
        components = []
        for node in self.nodes:
            if not visited[node]:
                component = bfs(node, visited)
                components.append(component)
        return components
                      
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
        if self.get_path_with_power(src,dest,float("inf"))!=None:
            self.power.sort()
            a = 0
            b = len(self.power)-1
            m = (a+b)//2
            while a < b :
                if self.get_path_with_power(src,dest,self.power[m])!=None:
                    b=m ##On n'exclut pas m
                else:
                    a=m+1
                m=(a+b)//2
            return self.get_path_with_power(src,dest,self.power[a]),self.power[a]
        raise Exception("Il n'y a pas de chemin entre src et dest")
 
    
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
                g.edges.append((node1, node2, power_min,1))
                g.power.append(power_min)
            elif len(edge) == 4:
                node1, node2, power_min, dist = int(edge[0]),int(edge[1]),int(edge[2]),float(edge[3]) #Pour pouvoir lire 10
                g.add_edge(node1, node2, power_min, dist)
                g.edges.append((node1, node2, power_min,dist))
                g.power.append(power_min)
            else:
                raise Exception("Format incorrect")
    return g

def kruskal(g):

    N=g.nb_nodes
    arcs=g.edges
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
    
def build_oriented_tree(g, root):
        # Construire un arbre orienté des enfants vers les parents
        oriented_tree = {root: []}
        queue = deque([root])
        visited = {root}
        while queue:
            parent = queue.popleft()
            for child in g.graph[parent]:
                if child[0] not in visited:
                    visited.add(child[0])
                    oriented_tree[child[0]] = [(parent,child[1],child[2])]
                    queue.append(child[0])
        return oriented_tree

        
def min_power_tree(tree,src,dest):
    # Remonter les ancêtres de src
    src_ancestors = []
    curr = src
    while curr!=1: #CHOIX ARBITRAIRE DE LA RACINE COMME ÉTANT 1
        src_ancestors.append([curr,tree[curr][0][1]])
        curr = tree[curr][0][0]
    src_ancestors.append([1,-1])
    # Remonter les ancêtres de dest
    dest_ancestors = []
    curr = dest
    while curr!=1: #CHOIX ARBITRAIRE DE LA RACINE COMME ÉTANT 1while curr!=1: #CHOIX ARBITRAIRE DE LA RACINE COMME ÉTANT 1
        dest_ancestors.append([curr,tree[curr][0][1]])
        curr = tree[curr][0][0]
    dest_ancestors.append([1,-1])
    # Trouver l'indice du premier ancêtre commun entre src et dest
    i = len(src_ancestors) - 1
    j = len(dest_ancestors) - 1
    while i >= 0 and j >= 0 and src_ancestors[i][0] == dest_ancestors[j][0]:
        i -= 1
        j -= 1
    # Concaténer les chemins de src et dest jusqu'à l'ancêtre commun
    path =src_ancestors[:i+2]
    path[i+1][1]=-1
    path.extend(reversed(dest_ancestors[:j+1]))
    power, chemin=max([x[1] for x in path]), [i[0] for i in path]
    return chemin,power

