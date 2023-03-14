import sys
sys.setrecursionlimit(500000)
from graph import Graph, graph_from_file, kruskal,build_oriented_tree,table_ancestors_power_2,depths_nodes,find_lca,min_power_tree
from UnionFind import UnionFind
from time import perf_counter
data_path="input/"
file_name1 = "network.00.in"
g1= graph_from_file(data_path+file_name1)
A=kruskal(g1)
T=build_oriented_tree(A,1)
Ancestors=table_ancestors_power_2(T)
print(Ancestors)
#D=depths_nodes(A)
#print(find_lca(47762,22199,D,Ancestors))
#print(min_power_tree(T,47762,22199))
