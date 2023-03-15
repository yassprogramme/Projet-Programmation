#%%
####PRÉPROCESSING POUR LA SÉANCE 2 ET 3
import sys
sys.setrecursionlimit(500000)
from graph import Graph, graph_from_file, kruskal,build_oriented_tree,min_power_tree,depths_nodes,table_ancestors_power_2,find_lca
from UnionFind import UnionFind

"On peut effectuer tout le processing en faisant des boucles for mais ça perd en lisibilité."

data_path="/Users/y.boukhateb/Desktop/COURS/Programmation/ensae-prog23/input/"
file_name1 = "network.1.in"
g1= graph_from_file(data_path+file_name1)
mst1=kruskal(g1)
T1=build_oriented_tree(mst1,1)
D1=depths_nodes(mst1)
Ancestors1=table_ancestors_power_2(T1)

file_name2 = "network.2.in"
g2 = graph_from_file(data_path+file_name2)
mst2=kruskal(g2)
T2=build_oriented_tree(mst2,1)
D2=depths_nodes(mst2)
Ancestors2=table_ancestors_power_2(T2)

file_name3 = "network.3.in"
g3 = graph_from_file(data_path+file_name3)
mst3=kruskal(g3)
T3=build_oriented_tree(mst3,1)
D3=depths_nodes(mst3)
Ancestors3=table_ancestors_power_2(T3)

file_name4 = "network.4.in"
g4 = graph_from_file(data_path+file_name4)
mst4=kruskal(g4)
T4=build_oriented_tree(mst4,1)
D4=depths_nodes(mst4)
Ancestors4=table_ancestors_power_2(T4)

file_name5 = "network.5.in"
g5= graph_from_file(data_path+file_name5)
mst5=kruskal(g5)
T5=build_oriented_tree(mst5,1)
D5=depths_nodes(mst5)
Ancestors5=table_ancestors_power_2(T5)

file_name6 = "network.6.in"
g6 = graph_from_file(data_path+file_name6)
mst6=kruskal(g6)
T6=build_oriented_tree(mst6,1)
D6=depths_nodes(mst6)
Ancestors6=table_ancestors_power_2(T6)

file_name7 = "network.7.in"
g7 = graph_from_file(data_path+file_name7)
mst7=kruskal(g7)
T7=build_oriented_tree(mst7,1)
D7=depths_nodes(mst7)
Ancestors7=table_ancestors_power_2(T7)

file_name8 = "network.8.in"
g8 = graph_from_file(data_path+file_name8)
mst8=kruskal(g8)
T8=build_oriented_tree(mst8,1)
D8=depths_nodes(mst8)
Ancestors8=table_ancestors_power_2(T8)

file_name9 = "network.9.in"
g9 = graph_from_file(data_path+file_name9)
mst9=kruskal(g9)
T9=build_oriented_tree(mst9,1)
D9=depths_nodes(mst9)
Ancestors9=table_ancestors_power_2(T9)

file_name10 = "network.10.in"
g10 = graph_from_file(data_path+file_name10)
mst10=kruskal(g10)
T10=build_oriented_tree(mst10,1)
D10=depths_nodes(mst10)
Ancestors10=table_ancestors_power_2(T10)


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





#%%
from time import perf_counter
def tps_calcul(T,x):
    tstart=perf_counter()
    route="routes."+str(x)+".in"
    with open(data_path+route, "r") as file:
        n=int(file.readline())
        for _ in range(5):
            trajet=file.readline().split()
            src,dest=int(trajet[0]),int(trajet[1])
            T.min_power(src,dest)[1] 
        tend=perf_counter()
    return ((tend-tstart)*n)/5


### TESTS DE TEMPS AVEC MIN_POWER DE LA QUESTION 6

file = "/Users/y.boukhateb/Desktop/COURS/Programmation/ensae-prog23/output/temps_calcul_S2Q1"
f = open(file, 'w')
f.write("temps de calcul : min_power Q6\n")

for x in range(1, 11):
    network = "network."+str(x)+".in"
    g=graph_from_file(data_path+network)
    t = tps_calcul(g,x)
    f.write("routes"+str(x)+": "+str(t)+"sec = "+str(t/60)+"min"+"\n")

f.close()






#%%
def tps_calcul2(T,x):
    tstart=perf_counter()
    route="routes."+str(x)+".in"
    with open(data_path+route, "r") as file:
        n=int(file.readline())
        for _ in range(n):
            trajet=file.readline().split()
            src,dest=int(trajet[0]),int(trajet[1])
            min_power_tree(T,src,dest)[1] 
        tend=perf_counter()
    return (tend-tstart)

t1=tps_calcul2(T1,1)
t2 = tps_calcul2(T2,2)
t3 = tps_calcul2(T3,3)
t4 = tps_calcul2(T4,4)
t5 = tps_calcul2(T5,5)
t6 = tps_calcul2(T6,6)
t7 = tps_calcul2(T7,7)
t8 = tps_calcul2(T8,8)
t9 = tps_calcul2(T9,9)
t10 = tps_calcul2(T10,10)

file = "/Users/y.boukhateb/Desktop/COURS/Programmation/ensae-prog23/output/temps_calcul_S2Q15"
f = open(file, 'w')
f.write("temps de calcul : min_power_tree Q15\n")
f.write("routes 1 :"+str(t1)+"sec =" +str(t1/60)+"min"+"\n")
f.write("routes 2 :"+str(t2)+"sec =" +str(t2/60)+"min"+"\n")
f.write("routes 3 :"+str(t3)+"sec =" +str(t3/60)+"min"+"\n")
f.write("routes 4 :"+str(t4)+"sec =" +str(t4/60)+"min"+"\n")
f.write("routes 5 :"+str(t5)+"sec =" +str(t5/60)+"min"+"\n")
f.write("routes 6 :"+str(t6)+"sec =" +str(t6/60)+"min"+"\n")
f.write("routes 7 :"+str(t7)+"sec =" +str(t7/60)+"min"+"\n")
f.write("routes 8 :"+str(t8)+"sec =" +str(t8/60)+"min"+"\n")
f.write("routes 9 :"+str(t9)+"sec =" +str(t9/60)+"min"+"\n")
f.write("routes 10 :"+str(t10)+"sec =" +str(t10/60)+"min"+"\n")
f.close()








# %%
def tps_calcul3(depth,ancestors,x):
    tstart=perf_counter()
    route="routes."+str(x)+".in"
    with open(data_path+route, "r") as file:
        n=int(file.readline())
        for _ in range(n):
            trajet=file.readline().split()
            src,dest=int(trajet[0]),int(trajet[1])
            find_lca(src,dest,depth,ancestors) 
        tend=perf_counter()
    return (tend-tstart)

t1=tps_calcul3(D1,Ancestors1,1)
t2 = tps_calcul3(D2,Ancestors2,2)
t3 = tps_calcul3(D3,Ancestors3,3)
t4 = tps_calcul3(D4,Ancestors4,4)
t5 = tps_calcul3(D5,Ancestors5,5)
t6 = tps_calcul3(D6,Ancestors6,6)
t7 = tps_calcul3(D7,Ancestors7,7)
t8 = tps_calcul3(D8,Ancestors8,8)
t9 = tps_calcul3(D9,Ancestors9,9)
t10 = tps_calcul3(D10,Ancestors10,10)

file = "/Users/y.boukhateb/Desktop/COURS/Programmation/ensae-prog23/output/temps_calcul_S3Q17"
f = open(file, 'w')
f.write("temps de calcul : min_power_tree Q17\n")
f.write("routes 1 :"+str(t1)+"sec =" +str(t1/60)+"min"+"\n")
f.write("routes 2 :"+str(t2)+"sec =" +str(t2/60)+"min"+"\n")
f.write("routes 3 :"+str(t3)+"sec =" +str(t3/60)+"min"+"\n")
f.write("routes 4 :"+str(t4)+"sec =" +str(t4/60)+"min"+"\n")
f.write("routes 5 :"+str(t5)+"sec =" +str(t5/60)+"min"+"\n")
f.write("routes 6 :"+str(t6)+"sec =" +str(t6/60)+"min"+"\n")
f.write("routes 7 :"+str(t7)+"sec =" +str(t7/60)+"min"+"\n")
f.write("routes 8 :"+str(t8)+"sec =" +str(t8/60)+"min"+"\n")
f.write("routes 9 :"+str(t9)+"sec =" +str(t9/60)+"min"+"\n")
f.write("routes 10 :"+str(t10)+"sec =" +str(t10/60)+"min"+"\n")
f.close()


# %%
