from UnionFind import UnionFind
from collections import deque
import heapq
from math import log2
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

##### SEANCE 1 QUESTION 3#######
    def get_path_with_power(self,src,dest,power):
        """""   Méthode get_path_with_power()
        Description : 
        -----------
        Donne un chemin entre deux neouds si c'est possible pour un camion de puissance power
        en effectuant un parcours en largeur BFS

        Inputs:
        -----
        src : noeud de départ
        dest : noeud d'arrivé
        power : la puissance du camion

        Outputs:
        -------
        Si i y a un chemin output = liste du chemin
        sinon None

        Complexity : O(N) BFS
        """
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
    
                    ##### SEANCE 1 QUESTION 5#######

    def get_min_path_with_power(self, src, dest, power): #Dijkstra
        ''' Méthode get_path_min_dist()
        Description :
        ------------
        La fonction retourne pour les chemins admissible avec la puissance power,
        le chemin de distance minimale par l'algorithme de Dijkstra
        Inputs:
        -----
        src: noeud de départ 
        dest: noeud d'arrivé 
        power: puissance du camion

        Outputs:
        ------
        Si src et dest ne sont pas dans la même composante connexe output = None
        sinon return un couple contenant le chemin et la puissance.
        
        Complexity : O(Nlog(N)) on parcourt chaque noeud mais trier à chaque fois
        '''

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

##### SEANCE 1 QUESTION 2#######
    def connected_components(self):
        """   Méthode connected_components()
        Description:
        -----------
        La fonction bfs trouve la composante connexe d'un noeud dans le graphe et on l'applique 
        pour tous les noeuds non visités

        input:
        -----
        une instance de Graph

        output:
        -------

        une liste contenant les composantes connexes

        Complexity : O(N^2) si tous les points sont isolés
        """  
        def bfs(start_node, visited):
            #Parcours en largeur du graphe
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
                component = bfs(node, visited)#composante associé au noeud tout en indiquant visité les noeuds dans sa composante connexe
                components.append(component)
        return components
                      
    def connected_components_set(self):
        """
        The result should be a set of frozensets (one per component), 
        For instance, for network01.in: {frozenset({1, 2, 3}), frozenset({4, 5, 6, 7})}
        """
        return set(map(frozenset, self.connected_components()))
    

    ##### SEANCE 1 QUESTION 6#######
    def min_power(self, src, dest):
        """""   Fonction : min_power
        Description:
        -----------
        Renvoie la puissance minimale que doit avoir un camion pour effectuer un trajet
        ------
        g : src :départ
            dest:arrivée

        output:
        -------
        La puissance minimale

        Complexity : O(Nlog(N)) car on trie les puissances. La dichtomie est en log(N) N nb d'arrêtes
        """
        if self.get_path_with_power(src,dest,float("inf"))!=None:
            self.power.sort()
            a = 0
            b = len(self.power)-1
            m = (a+b)//2
            while a < b :
                if self.get_path_with_power(src,dest,self.power[m])!=None:
                    b=m #on n'exclut pas m car c'est peut-être le dernier entier qui fonctionne
                else:
                    a=m+1
                m=(a+b)//2
            return self.get_path_with_power(src,dest,self.power[a]),self.power[a]
        raise Exception("Il n'y a pas de chemin entre src et dest")
 
##### SEANCE 1 QUESTION 1#######
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

    Complexity : O(Nb d'arrêtes)
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
                g.edges.append((node1, node2, power_min,dist))#On récupére les arrêtes pour Kruskal
                g.power.append(power_min)#On récupère les puissances pour effectuer min_power Q6
            else:
                raise Exception("Format incorrect")
    return g

#######QUESTION 13#######

def kruskal(g):
    """""   Fonction : kruskal
    Description:
    -----------
    Permet d'envoyer un objet de la Class Graph qui est un arbre couvrant de poids minimal.
    input:
    ------
    g : une instance de la classe graph

    output:
    -------
    une instance de la classe graph

    Complexity : O(Nlog(N )). La complexité et l'algorithme sera démontré dans le rapport final
    """

    N=g.nb_nodes
    arcs=g.edges #Les arcs sont récupérés directement dans la lecture du fichier pour gagner du temps
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
    #####SEANCE 2 QUESTION 14 : PRÉPROCESSING#######
def build_oriented_tree(g, root):
    """""   Fonction : kruskal
    Description:
    -----------
    Permet d'envoyer un objet de la Class Graph qui est un arbre couvrant de poids minimal.
    input:
    ------
    g : une instance de la classe graph

    output:
    -------
    une instance de la classe graph
    
    Complexity : c'est un BFS donc O(N)

    """
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

        #####SEANCE 2 QUESTION 14#######
def min_power_tree(tree,src,dest):
    """""   Fonction : min_power_tree
    Description:
    -----------
    trouve le chemin entre deux noeuds dans un arbre en remontant les ancêtres pour touver 
    l'ancêtre minimum. On peut utiliser la profondeur des noeuds pour aller plus vite mais c'est déjà assez
    rapide sans. On utilise la profondeur dans la séance 3 où le même principe est repris
    pour aller justement beaucoup plus vite.

    Input:
    ------
    src : noeud de départ
    type : int

    dest : noeud d'arrivé
    type : int

    tree : arbre 

    output : 
    -------
    un couple contenant la puissance minimal et le chemin de src à dest

    Complexity : O(N) dans le pire cas. On se retrouve à parcourir tous les sommets

    """
    # Remonter les ancêtres de src
    src_ancestors = []
    curr = src
    while curr!=1: #CHOIX ARBITRAIRE DE LA RACINE COMME ÉTANT 1
        src_ancestors.append([curr,tree[curr][0][1]])
        curr = tree[curr][0][0]
    src_ancestors.append([1,0])
    # Remonter les ancêtres de dest
    dest_ancestors = []
    curr = dest
    while curr!=1: #CHOIX ARBITRAIRE DE LA RACINE COMME ÉTANT 1
        dest_ancestors.append([curr,tree[curr][0][1]])
        curr = tree[curr][0][0]
    dest_ancestors.append([1,0])
    # Trouver l'indice du premier ancêtre commun entre src et dest. On peut utiliser la profondeur pour éviter de remonter jusqu'à la racine
    i = len(src_ancestors) - 1
    j = len(dest_ancestors) - 1
    while i >= 0 and j >= 0 and src_ancestors[i][0] == dest_ancestors[j][0]:
        i -= 1
        j -= 1
    # Concaténer les chemins de src et dest jusqu'à l'ancêtre commun
    path =src_ancestors[:i+2]
    path[i+1][1]=0 #Car on ne prend en compte la puissance de l'ancêtre vers son parent
    path.extend(reversed(dest_ancestors[:j+1]))
    power, chemin=max([x[1] for x in path]), [i[0] for i in path]
    return chemin,power

#***********************************************************************************************#

#*******SEANCE 3**********####
def table_ancestors_power_2(tree):#Arbre orienté enfants vers parents
    """""   Fonction : table_ancestors_power_2 Préproccesing
    Description:
    -----------
    Dans un dictionnaire, on stocke pour chaque noeud, l'ancêtre 2^j au dessus de lui
      et la puissance pour l'atteindre pour tout j entre 0 et le log2(N)
    input:
    ------
    Tree: L'arbre orienté

    output:
    -------
    Un dictionnaire

    Complexité : O(Vlog(V)) On a deux boucles imbriquées : une de taille log2(N) et l'autre de taille N

    """
    N=len(tree)
    up={k: [(-1,0) for i in range(int(log2(N))+1)] for k in tree.keys()} #int(log2(N)) est le max des ancêtres en puissance de 2 possibles
    tree[1]=[(-1,0,0)]#On définit un ancêtre
    for v in tree.keys():
        up[v][0]=(tree[v][0][0],tree[v][0][1])
    for j in range(1,int(log2(N))+1):
        for v in tree.keys():
            if up[v][j-1][0]!=-1 and up[up[v][j-1][0]][j-1][0]!=-1:
                up[v][j]=up[up[v][j-1][0]][j-1][0],max(up[v][j-1][1],up[up[v][j-1][0]][j-1][1]) # On fait le max entre src et son ancêtre 2^(j-1) et entre ce dernier et l'ancêtre 2^j
            elif up[v][j-1][0]!=-1 and up[up[v][j-1][0]][j-1][0]==-1:
                up[v][j]=up[up[v][j-1][0]][j-1][0],0 # C'est juste pour ramener la puissance à 0 quand on sort de l'arbre
    return up

def depths_nodes(mst): ## MST fait par kruskal, profondeur fait à partir de la racine 1
    """""   Fonction : depths_nodes Préproccesing
    Description:
    -----------
    On a 1 comme racine fixé arbitrairement pour tous les MST. Ainsi, dans un dictionnaire on récupère
    la profondeur de chaque noeud dans le graphe par rapport à 1 par un BFS.
    input:
    ------
    Tree: L'arbre orienté

    output:
    -------
    Un dictionnaire des profondeurs

    Complexité : O(V) On parcourt tous les noeuds

    """
    depths={node:0 for node in mst.nodes}
    Bdepths={node:0 for node in mst.nodes}
    queue = deque([1])
    visited = {1}
    while queue:
        noeud = queue.popleft()
        for child in mst.graph[noeud]:
            if child[0] not in visited:
                visited.add(child[0])
                depths[child[0]]=depths[noeud]+1
                queue.append(child[0])
    return depths


#Question 16
def find_lca(src, dest, depth, ancestors):
    """""   Fonction : find_lca
    Description:
    -----------
    On remonte l'élément entre src et dest le plus bas pour les avoir au même niveau, puis on les 
    remonte au fur et à mesure pour arriver au LCA tout en conservant la puissance au cours de cette
    montée. On peut remonter uniquement en puissance de 2 mais tous les ancêtres de l'arbre sont
    accessiblesnotamment grâce à la décomposition en base 2 des entiers
    input:
    ------
    Tree: L'arbre orienté

    output:
    -------
    La puissance minimale entre src et dest
    
    Complexité : O(ln(N)) car on parcourt deux fois une boucle de taille ln(N)

    """
    log_N=int(log2(len(depth)))
    # On vérifie qui est le plus profond
    if depth[src] < depth[dest]:
        src, dest = dest, src
    # On remonte src à la même hauteur que dest
    pow=0
    for i in range(log_N,-1,-1):
        if depth[src]-2**i>=depth[dest]:
            pow=max(ancestors[src][i][1],pow)
            src=ancestors[src][i][0]
    if src==dest:
        return pow
    for k in range(log_N,-1,-1):
        if (ancestors[dest][k][0]!=-1) and (ancestors[dest][k][0]!=ancestors[src][k][0]):
            psrc=ancestors[src][k][1] # on conserve la puissance max du saut entre src et son ancêtre 2^j
            pdest=ancestors[dest][k][1]# on conserve la puissance max du saut entre dest et son ancêtre 2^j
            dest=ancestors[dest][k][0]
            src=ancestors[src][k][0]
            pow=max(pow,psrc,pdest) # On conserve la puissance max entre tous les sauts et les sauts précédents
    return max(pow,ancestors[src][0][1],ancestors[dest][0][1])



