class UnionFind:
    """""   Class UnionFind
    Attributs : 
    -----------
    parent : liste
    rank : liste 

    Methodes : 
    ----------

    get_parent(): obtenir le parent d'un noeud qui est un représentant d'un groupe de noeuds
    Union(): permet de réunir deux groupes de noeuds
    """

    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
        
    def Union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            else:
                self.parent[root_x] = root_y
                if self.rank[root_x] == self.rank[root_y]:
                    self.rank[root_y] += 1

