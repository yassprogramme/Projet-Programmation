from graph import Graph, graph_from_file, kruskal, min_power 
from UnionFind import UnionFind
data_path = "input/"
file_name = "network.00.in"
g = graph_from_file(data_path + file_name)


from graph import Graph, graph_from_file
from time import perf_counter

def tps_calcul(x):
# Start the stopwatch / counter
    t1_start = perf_counter()
    route="routes.1.in"
    #network="network."+str(x)+".in"
    #g=graph_from_file(data_path+"network.1.in")
    with open(data_path+route, "r") as file:
        n=int(file.readline())
        g1=[None for k in range(10)]
        for k in range(1):
            trajet=file.readline().split()
            src,dest=int(trajet[0]),int(trajet[1])
            g1[k]=(src,dest)
            #g.min_power(src,dest)
        t1_stop = perf_counter()
    return g1,t1_stop-t1_start
    #return ((t1_stop-t1_start)*n)/10


# Stop the stopwatch / counter
def temps_moyen():
    d=0
    for x in range(1,11):
        d+=tps_calcul(x)
    return d