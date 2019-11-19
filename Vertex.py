class Vertex:

    def __init__(self, val):
        self.Value = val
  
class SimpleGraph:
	
    def __init__(self, size):
        self.max_vertex = size
        self.m_adjacency = [[0] * size for _ in range(size)]
        self.vertex = [None] * size
        
    def AddVertex(self, v):
        if len(self.vertex) >= self.max_vertex:
            return
        new_vertex = Vertex(v)
        self.vertex.append(new_vertex)
        # ваш код добавления новой вершины 
        # с значением value 
        # в свободное место массива vertex

    # здесь и далее, параметры v -- индекс вершины
    # в списке  vertex
    def RemoveVertex(self, v):
        if v > len(self.vertex) - 1:
            return
        chained_with = []
        adj_vertex_ind = 0
        for edge in self.m_adjacency[v]:
            if edge == 1:
                chained_with.append(adj_vertex_ind)
            adj_vertex_ind += 1
        for adj_vertex_i in chained_with:
            self.RemoveEdge(v, adj_vertex_i)
        # ваш код удаления вершины со всеми её рёбрами

	
    def IsEdge(self, v1, v2):
        if v1 > len(self.vertex) - 1 or v2 > len(self.vertex) - 1:
            return False
        return self.m_adjacency[v1][v2] == 1
        # True если есть ребро между вершинами v1 и v2
	
    def AddEdge(self, v1, v2):
        if v1 > len(self.vertex) - 1 or v2 > len(self.vertex) - 1:
            return
        self.m_adjacency[v1][v2] = 1
        self.m_adjacency[v2][v1] = 1
        # добавление ребра между вершинами v1 и v2
	
    def RemoveEdge(self, v1, v2):
        if v1 > len(self.vertex) - 1 or v2 > len(self.vertex) - 1:
            return
        self.m_adjacency[v1][v2] = 0
        self.m_adjacency[v2][v1] = 0
        # удаление ребра между вершинами v1 и v2
