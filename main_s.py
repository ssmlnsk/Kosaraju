from collections import defaultdict


class GraphSCC:
    """
    Структура данных
    """
    def __init__(self, vertex):
        """
        Инициализация графа
        :param vertex: максимальный размер графа
        """
        self.V = vertex
        self.graph = defaultdict(list)
        self.cons = []

    def add_edge(self, s, d):
        """
        Функция, реализующая добавление соединения
        :param s: первый элемент графа
        :param d: второй элемент графа
        :return: None
        """
        self.graph[s].append(d)

    def dfs(self, d, visited_vertex):
        """
        Вспомогательная функция к print_scc
        :param d: второй элемент графа
        :param visited_vertex: посещенная вершина
        :return: None
        """
        visited_vertex[d] = True
        self.cons.append(d)
        for i in self.graph[d]:
            if not visited_vertex[i]:
                self.dfs(i, visited_vertex)

    def fill_order(self, d, visited_vertex, stack):
        """
        Функция заполнения стека
        :param d: второй элемент графа
        :param visited_vertex: посещенная вершина
        :param stack: стек
        :return: None
        """
        visited_vertex[d] = True
        for i in self.graph[d]:
            if not visited_vertex[i]:
                self.fill_order(i, visited_vertex, stack)
        stack = stack.append(d)

    def transpose(self):
        """
        Функция, возвращающая словарь
        :return: g
        """
        g = GraphSCC(self.V)

        for i in self.graph:
            for j in self.graph[i]:
                g.add_edge(j, i)
        return g

    def print_scc(self):
        """
        Функция, выводящая компоненты с сильной связаностью
        :return: cons_lst
        """
        stack = []
        visited_vertex = [False] * self.V

        for i in range(self.V):
            if not visited_vertex[i]:
                self.fill_order(i, visited_vertex, stack)

        gr = self.transpose()

        visited_vertex = [False] * self.V

        cons_lst = []
        while stack:
            i = stack.pop()
            if not visited_vertex[i]:
                gr.cons = []
                gr.dfs(i, visited_vertex)
                cons_lst.append(gr.cons)
        return cons_lst


if __name__ == "__main__":
    g = GraphSCC(8)
    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    g.add_edge(2, 4)
    g.add_edge(3, 0)
    g.add_edge(4, 5)
    g.add_edge(5, 6)
    g.add_edge(6, 4)
    g.add_edge(6, 7)
    print(g.print_scc())
