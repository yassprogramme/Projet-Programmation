class UnionFind:
    """Cette classe permet de gérer les ensembles disjoints. Deux éléments sont considérés dans le même ensemble 
    s'ils ont le même parent"""
    parent={}

    #Création de n ensembles disjoints
    def __init__(self,N):
        for i in range(N):
            self.parent[i]=i
    
    #Fonction Find 
    def find(self,k):
        if self.parent[k]==k:
            return k
        return self.find(self.parent[k])
    
    #Fonction Union
    def Union(self,a,b):
        x=self.find(a)
        y=self.find(b)
        self.parent[x]=y
    

