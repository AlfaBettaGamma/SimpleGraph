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
        '''ваш код добавления новой вершины 
        с значением value 
        в свободное место массива vertex
        здесь и далее, параметры v -- индекс вершины
        в списке  vertex
        '''
        for i in range(len(self.vertex)):
            if self.vertex[i] != None and self.vertex[i].Value == v:
                return
            if self.vertex[i] == None:
                my_vertex = Vertex(v)
                self.vertex[i] = my_vertex
                return
        
    def RemoveVertex(self, v):
        '''ваш код удаления вершины со всеми её рёбрами'''
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
        

	
    def IsEdge(self, v1, v2):
        if v1 > len(self.vertex) - 1 or v2 > len(self.vertex) - 1:
            return False
        return self.m_adjacency[v1][v2] == 1
        # True если есть ребро между вершинами v1 и v2
	
    def AddEdge(self, v1, v2):
        '''добавление ребра между вершинами v1 и v2'''
        if v1 > len(self.vertex) - 1 or v2 > len(self.vertex) - 1:
            return
        self.m_adjacency[v1][v2] = 1
        self.m_adjacency[v2][v1] = 1
        
	
    def RemoveEdge(self, v1, v2):
        '''удаление ребра между вершинами v1 и v2'''
        if v1 > len(self.vertex) - 1 or v2 > len(self.vertex) - 1:
            return
        self.m_adjacency[v1][v2] = 0
        self.m_adjacency[v2][v1] = 0
        

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
        '''узлы задаются позициями в списке vertex
        возвращается список узлов -- путь из VFrom в VTo
        или [] если пути нету
        '''
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


    def BreadthFirstSearch(self, VFrom, VTo):
        ''' узлы задаются позициями в списке vertex
        возвращается список узлов -- путь из VFrom в VTo
        или [] если пути нету'''
        '''Поиск пути от одного узла к другому через обход в глубину'''
        if VFrom >= len(self.vertex) or VTo >= len(self.vertex) or VFrom < 0 or VTo < 0:
            return []
        if self.vertex[VFrom] == None or self.vertex[VTo] == None:
            return []
        elif VFrom == VTo:
            return [self.vertex[VFrom]]
        else:
            vertex_deque = []
            path_stack = []
            count_iter = 0
            current_vertext = VFrom
            path_stack.append(current_vertext)
            while count_iter <= len(self.m_adjacency):
                self.vertex[current_vertext].Hit = True
                for j in range(len(self.m_adjacency)):
                    if self.m_adjacency[current_vertext][j] == 1 and j == VTo:
                        path_stack.append(j)
                        index = path_stack[len(path_stack)-1]
                        result_path = []
                        if len(path_stack) > 2:
                            result_path.append(index)
                            while index != 0:
                                for k in range(len(self.m_adjacency)):
                                    if self.m_adjacency[index][k] == 1 and path_stack.count(k) == 1:
                                        result_path.append(k)
                                        index = k
                                        break
                            result_path.reverse()
                        else:
                            result_path = path_stack
                        for i in range(len(result_path)):
                            result_path[i] = self.vertex[result_path[i]]
                        return result_path

                for j in range(len(self.m_adjacency)):
                    if self.m_adjacency[current_vertext][j] == 1 and j != VTo and self.vertex[j].Hit == False:
                        if len(vertex_deque) > 0:
                            if vertex_deque.count(j) == 0:
                                vertex_deque.append(j)
                        else:
                            vertex_deque.append(j)
                if len(vertex_deque) != 0:
                    current_vertext = vertex_deque.pop(0)
                    path_stack.append(current_vertext)
                else:
                    return []
                count_iter += 1

