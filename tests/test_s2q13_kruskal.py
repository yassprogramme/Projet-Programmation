# This will work if ran from the root folder.
import sys 
sys.path.append("delivery_network")

from graph import Graph, graph_from_file, kruskal

import unittest   # The test framework

class Test_GraphCC(unittest.TestCase):
    def test_network0(self):
        g = graph_from_file("input/network.01.in")
        g_mst = kruskal(g)
        mst_expected="Le graphe n'est pas connexe"
        self.assertEqual(g_mst, {frozenset({1, 2, 3, 4, 5, 6, 7, 8, 9, 10})})

    def test_network1(self):
        g = graph_from_file("input/network.01.in")
        g_mst = kruskal(g)

        self.assertEqual(g_mst, {frozenset({1, 2, 3}), frozenset({4, 5, 6, 7})})

    def test_network2(self):
        g = graph_from_file("input/network.04.in")
        g_mst = g.connected_components_set()
        self.assertEqual(g_mst, {frozenset({1, 2, 3,4}),frozenset({5}),frozenset({6}),frozenset({7}),frozenset({8}),frozenset({9}),frozenset({10})})

if __name__ == '__main__':
    unittest.main()
