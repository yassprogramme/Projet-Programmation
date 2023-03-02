from graph import Graph, graph_from_file, connected_components


data_path = "input/"
file_name = "network.01.in"

g = graph_from_file(data_path + file_name)
print(connected_components(g))