# on fait les tests des fonctions :
# - graph_from_file()
# - connected.components_set()
# - get_path_with_power()
# - get_min_path_with_power()
# - min_power()



import sys 
sys.path.append("delivery_network")

from graph import graph_from_file
import unittest   # The test framework

class Test_MinimalPower(unittest.TestCase):
    def test_network03(self):
        g = graph_from_file("input/network.03.in")
        self.assertEqual(g.nb_nodes, 10)
        self.assertEqual(g.nb_edges, 4)
        self.assertEqual(g.graph[1][0], (2, 10, 1))
        self.assertEqual(g.graph[6], [])
        self.assertEqual(g.nodes, [i for i in range(1, 11)])

    def test_network03(self):
        g = graph_from_file("input/network.03.in")
        cc = g.connected_components_set()
        c ={frozenset({9}), frozenset({8}), frozenset({7}), frozenset({6}), frozenset({10}) ,frozenset({5}), frozenset({1, 2, 3, 4})}
        self.assertEqual(cc, c)

    def test_network01(self):
        g = graph_from_file("input/network.01.in")
        self.assertEqual(g.get_path_with_power(1, 4, 1), None)
        self.assertEqual(g.get_path_with_power(5, 6, 2), [5, 7, 6])
    
    def test_network05(self):
        g = graph_from_file("input/network.05.in")
        self.assertEqual(g.get_min_path_with_power(4, 2, 6), [4, 1, 2])

    def test_network02(self):
        g = graph_from_file("input/network.02.in")
        self.assertEqual(g.min_power(1, 3)[0], [1, 4, 3])
        self.assertEqual(g.min_power(1, 3)[1], 4)

if __name__ == '__main__':
    unittest.main()