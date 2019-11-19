import unittest
from Vertex import Vertex, SimpleGraph
class ls2_test(unittest.TestCase):

    def setUp(self):
        pass

    def test_add_first_vertex(self):
        new_graph = SimpleGraph(5)
        new_graph.AddVertex(15)
        self.assertEqual(new_graph.vertex[0].Value, 15)

    def test_add_vertex(self):
        new_graph = SimpleGraph(5)
        new_graph.AddVertex(15)
        new_graph.AddVertex(18)
        new_graph.AddVertex(224)
        new_graph.AddVertex(235)
        new_graph.AddVertex(257)
        new_graph.AddVertex(678)
        new_graph.AddVertex(19)
        self.assertEqual(len(new_graph.vertex), 5)
        self.assertEqual(new_graph.vertex[4].Value, 257)
        for row in new_graph.m_adjacency:
            for edge in row:
                self.assertEqual(edge, 0)

    def test_add_edge(self):
        new_graph = SimpleGraph(5)
        new_graph.AddVertex(15)
        new_graph.AddVertex(18)
        new_graph.AddVertex(224)
        new_graph.AddVertex(235)
        new_graph.AddVertex(257)
        new_graph.AddVertex(678)
        new_graph.AddEdge(0, 4)
        self.assertEqual(new_graph.m_adjacency[0][4], 1)
        self.assertEqual(new_graph.m_adjacency[4][0], 1)
        new_graph.AddEdge(3, 2)
        self.assertEqual(new_graph.m_adjacency[2][3], 1)
        self.assertEqual(new_graph.m_adjacency[3][2], 1)
        new_graph.AddEdge(0, 0)
        self.assertEqual(new_graph.m_adjacency[0][0], 1)
        self.assertEqual(new_graph.m_adjacency[0][0], 1)

    def test_remove_edge(self):
        new_graph = SimpleGraph(5)
        new_graph.AddVertex(1)
        new_graph.AddVertex(15)
        new_graph.AddVertex(12)
        new_graph.AddEdge(0, 1)
        self.assertEqual(new_graph.m_adjacency[0][1], 1)
        self.assertEqual(new_graph.m_adjacency[1][0], 1)
        new_graph.RemoveEdge(0, 1)
        self.assertEqual(new_graph.m_adjacency[0][1], 0)
        self.assertEqual(new_graph.m_adjacency[1][0], 0)
        new_graph.AddEdge(0, 0)
        self.assertEqual(new_graph.m_adjacency[0][0], 1)
        self.assertEqual(new_graph.m_adjacency[0][0], 1)
        new_graph.RemoveEdge(0, 0)
        self.assertEqual(new_graph.m_adjacency[0][0], 0)
        self.assertEqual(new_graph.m_adjacency[0][0], 0)

    def test_remove_vertex(self):
        new_graph = SimpleGraph(5)
        new_graph.AddVertex(1)
        new_graph.AddVertex(15)
        new_graph.AddVertex(12)
        new_graph.AddEdge(0, 1)
        new_graph.AddEdge(0, 2)
        self.assertEqual(new_graph.m_adjacency[0][1], 1)
        self.assertEqual(new_graph.m_adjacency[1][0], 1)
        self.assertEqual(new_graph.m_adjacency[0][2], 1)
        self.assertEqual(new_graph.m_adjacency[2][0], 1)
        new_graph.RemoveVertex(0)
        self.assertEqual(new_graph.m_adjacency[0][1], 0)
        self.assertEqual(new_graph.m_adjacency[1][0], 0)
        self.assertEqual(new_graph.m_adjacency[0][2], 0)
        self.assertEqual(new_graph.m_adjacency[2][0], 0)

    def tearDown(self):
        pass

unittest.main()