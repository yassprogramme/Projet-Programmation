import sys
sys.setrecursionlimit(500000)

from graph import Graph, graph_from_file, kruskal
from UnionFind import UnionFind
data_path = "input/"
file_name = "network.5.in"
g = graph_from_file(data_path+file_name)
print(g.min_power(1008,71))
 


from graph import Graph, graph_from_file
from time import perf_counter

def tps_calcul(x):
    tstart=perf_counter()
    route="routes."+str(x)+".in"
    network="network."+str(x)+".in"
    g=graph_from_file(data_path+ network)
    with open(data_path+route, "r") as file:
        n=int(file.readline())
        for k in range(10):
            trajet=file.readline().split()
            src,dest=int(trajet[0]),int(trajet[1])
            g.min_power(src,dest)
        tend=perf_counter()
    return((tend-tstart)*n)/10

#print(tps_calcul(4))

   