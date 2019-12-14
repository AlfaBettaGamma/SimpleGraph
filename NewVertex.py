class Vertex:

    def __init__(self, val):
        self.Value = val
        self.Hit = False
  
class SimpleGraph:
	
    def __init__(self, size):
        self.max_vertex = size
        self.m_adjacency = [[0] * size for _ in range(size)]
        self.vertex = [None] * size
        
    def AddVertex(self, v):
        for ind in range(self.max_vertex):
            if self.vertex[ind] is None:
                self.vertex[ind] = Vertex(v)
                break
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

    def PrintAllAdjacency(self):
        print('Vertext:')
        for vert in self.vertex:
            if vert != None:
                print(vert.Value,' ', end ='')
            else:
                print('None ', end='')
        print()
        print('m_adjacency:')
        for i in self.m_adjacency:
            for j in i:
                print ("{:4d}".format(j), end ="")
            print()

    def DepthFirstSearch(self, VFrom, VTo):
        # узлы задаются позициями в списке vertex
        # возвращается список узлов -- путь из VFrom в VTo
        # или [] если пути нету
        stack = []
        for vertex in self.vertex:
            if vertex:
                vertex.Hit = False
            
        stack.append(self.vertex[VFrom])
        self.vertex[VFrom].Hit = True
        
        while len (stack) > 0:
            if self.m_adjacency[VFrom][VTo]:
                stack.append(self.vertex[VTo])
                return stack
            else:
                for vertex in self.vertex:
                    if not vertex.Hit and self.m_adjacency[VFrom][self.vertex.index(vertex)]:
                        vertex.Hit = True
                        stack.append(vertex)
                        VFrom = self.vertex.index(vertex)
                        del_stack = False
                        break
                    del_stack = True
                if del_stack:
                    del stack[-1]
                    if len (stack) > 0:
                        VFrom = self.vertex.index(stack[-1])
        
        return stack


my_graph = SimpleGraph(9)
my_graph.AddVertex('A')
my_graph.AddVertex('B')
my_graph.AddVertex('C')
my_graph.AddVertex('D')
my_graph.AddVertex('E')
my_graph.AddVertex('F')
my_graph.AddVertex('G')
my_graph.AddVertex('H')
my_graph.AddVertex('I')
my_graph.AddEdge(0,1)
my_graph.AddEdge(0,3)
my_graph.AddEdge(1,0)
my_graph.AddEdge(1,4)
my_graph.AddEdge(1,2)
my_graph.AddEdge(2,1)
my_graph.AddEdge(2,5)
my_graph.AddEdge(3,0)
my_graph.AddEdge(3,6)
my_graph.AddEdge(4,1)
my_graph.AddEdge(4,7)
my_graph.AddEdge(5,2)
my_graph.AddEdge(5,8)
my_graph.AddEdge(6,3)
my_graph.AddEdge(6,7)
my_graph.AddEdge(7,4)
my_graph.AddEdge(7,6)
my_graph.AddEdge(7,8)
my_graph.AddEdge(8,7)
my_graph.AddEdge(8,5)
my_graph.AddEdge(0,4)
my_graph.AddEdge(4,8)
my_graph.AddEdge(8,4)
my_graph.AddEdge(4,0)
#my_graph.RemoveEdge(0, 3)
#my_graph.RemoveEdge(3, 1)
my_graph.PrintAllAdjacency()
path = my_graph.DepthFirstSearch(8, 8)
for item in path:
    print(item.Value, ' ', end='')