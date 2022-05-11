import unittest
from main_s import GraphSCC


class MyTestCase(unittest.TestCase):
    def test_add_edge(self):
        g = GraphSCC(4)
        g.add_edge(0, 1)
        g.add_edge(1, 2)
        g.add_edge(2, 3)
        self.assertEqual(dict(g.graph), {0: [1], 1: [2], 2: [3]})

    def test_print_scc(self):
        g = GraphSCC(5)
        g.add_edge(0, 1)
        g.add_edge(1, 2)
        g.add_edge(2, 3)
        g.add_edge(3, 4)
        g.add_edge(4, 2)
        result = g.print_scc()
        self.assertEqual(result, [[0], [1], [2, 4, 3]])


if __name__ == '__main__':
    unittest.main()
