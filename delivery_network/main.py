#%%
import sys
sys.setrecursionlimit(500000)
from graph import Graph, graph_from_file, kruskal,build_oriented_tree,min_power_tree
from UnionFind import UnionFind

data_path="/Users/y.boukhateb/Desktop/COURS/Programmation/ensae-prog23/input/"
file_name1 = "network.1.in"
g1= graph_from_file(data_path+file_name1)
mst1=kruskal(g1)
T1=build_oriented_tree(mst1,1)

file_name2 = "network.2.in"
g2 = graph_from_file(data_path+file_name2)
mst2=kruskal(g2)
T2=build_oriented_tree(mst2,1)

file_name3 = "network.3.in"
g3 = graph_from_file(data_path+file_name3)
mst3=kruskal(g3)
T3=build_oriented_tree(mst3,1)

file_name4 = "network.4.in"
g4 = graph_from_file(data_path+file_name4)
mst4=kruskal(g4)
T4=build_oriented_tree(mst4,1)

file_name5 = "network.5.in"
g5= graph_from_file(data_path+file_name5)
mst5=kruskal(g5)
T5=build_oriented_tree(mst5,1)

file_name6 = "network.6.in"
g6 = graph_from_file(data_path+file_name6)
mst6=kruskal(g6)
T6=build_oriented_tree(mst6,1)

file_name7 = "network.7.in"
g7 = graph_from_file(data_path+file_name7)
mst7=kruskal(g7)
T7=build_oriented_tree(mst7,1)

file_name8 = "network.8.in"
g8 = graph_from_file(data_path+file_name8)
mst8=kruskal(g8)
T8=build_oriented_tree(mst8,1)

file_name9 = "network.9.in"
g9 = graph_from_file(data_path+file_name9)
mst9=kruskal(g9)
T9=build_oriented_tree(mst9,1)

file_name10 = "network.10.in"
g10 = graph_from_file(data_path+file_name10)
mst10=kruskal(g10)
T10=build_oriented_tree(mst10,1)
#%%
data_path1="/Users/y.boukhateb/Desktop/COURS/Programmation/ensae-prog23/input/"
data_path2="/Users/y.boukhateb/Desktop/COURS/Programmation/ensae-prog23/output/"
def routes_out(T,x):
    f=open(data_path2+"routes."+str(x)+".out","w")  
    with open(data_path1+"routes."+str(x)+".in","r") as file:
        n=file.readline()
        f.write(n)
        for _ in range(int(n)):
            city1,city2,utility=file.readline().split()
            p=str(min_power_tree(T,int(city1),int(city2))[1])
            f.write(city1+" "+city2+" "+utility+" "+p+"\n") 
    f.close()

routes_out(T1,1)
routes_out(T2,2)
routes_out(T3,3)
routes_out(T4,4)
routes_out(T5,5)
routes_out(T6,6)
routes_out(T7,7)
routes_out(T8,8)
routes_out(T9,9)
routes_out(T10,10)

# %%
#%%
from time import perf_counter
def tps_calcul(T,x):
    tstart=perf_counter()
    route="routes."+str(x)+".in"
    with open(data_path+route, "r") as file:
        n=int(file.readline())
        for k in range(10):
            trajet=file.readline().split()
            src,dest=int(trajet[0]),int(trajet[1])
            min_power_tree(T,src,dest)[1] 
        tend=perf_counter()
    return(tend-tstart)

print(tps_calcul(T9,9))

### TESTS DE TEMPS AVEC MIN_POWER
'''
Routes 1 : 0.04116571199999998sec
Routes 2 : 134151.57678sec=37h
Routes 3 : 1009644.5106sec=280h=12j
Routes 4 : 2368088.8504sec=657h=27j
Routes 5 : 636144.64528sec=178h=7j
Routes 6 : 1613156.6403999997sec=448h=19j
Routes 7 : 3110135.2003999995sec=863h=36j
Routes 8 : 2393239.1288000005sec=665h=28j
Routes 9 : 2271053.4034000007sec=630h=26j
Routes 10 : 1975235.3881999995sec=549h=23j
'''
