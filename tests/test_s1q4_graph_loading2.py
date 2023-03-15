import sys 
sys.path.append("delivery_network/")

import unittest 
from graph import Graph, graph_from_file

class Test_GraphLoading(unittest.TestCase):
    def test_network04(self):
            g = graph_from_file("input/network.04.in")
            self.assertEqual(g.nb_nodes, 10)
            self.assertEqual(g.nb_edges, 4)
            self.assertEqual(g.graph[1][0][2], 6)

    def test_network6(self):
            g = graph_from_file("input/network.6.in")
            self.assertEqual(g.nb_nodes, 200000)
            self.assertEqual(g.nb_edges, 300000)
            self.assertEqual(g.graph[8][1][2], 8073)



if __name__ == '__main__':
    unittest.main()
