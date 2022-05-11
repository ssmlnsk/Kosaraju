import os.path
import matplotlib.pyplot as plt
import networkx as nx
from main_s import GraphSCC
from sql import DBFile


class Facade:
    """
    Класс фасада
    """
    def __init__(self, w):
        """
        Инициализация окна
        :param w: виджет
        """
        self.w = w
        self.gui_edge_list = [(0, 1)]

    def save(self):
        """
        Функция сохранения данных в базу данных
        :return: None
        """
        text = self.w.linefile.text()
        if text:
            db = DBFile(text)
            db.save_db(self.gui_edge_list)

    def load(self):
        """
        Функция загрузки данных из базы данных
        :return: None
        """
        text = self.w.linefile.text()
        if os.path.exists('data/' + text + '.db'):
            db = DBFile(text)
            self.gui_edge_list = db.load_db()
        self.redraw()

    def clear(self):
        """
        Фунция очистки окна
        :return: None
        """
        self.gui_edge_list = [(0, 1)]
        self.redraw()

    def add_edge(self):
        """
        Функция добавления ребра
        :return: None
        """
        n1 = self.w.line1.value()
        n2 = self.w.line2.value()
        self.gui_edge_list.append((n1, n2))
        self.redraw()

    def redraw(self):
        """
        Функция перерисовки графа
        :return: None
        """
        plt.clf()
        self.g = nx.DiGraph()

        edges_list = self.gui_edge_list
        m = 0
        for i in edges_list:
            if max(i) > m:
                m = max(i)
        gscc = GraphSCC(m + 1)

        for edge in edges_list:
            gscc.add_edge(edge[0], edge[1])

        self.g.add_edges_from(edges_list, color='grey')
        cons_list = gscc.print_scc()
        for edges in cons_list:
            if len(edges) > 2:
                for n in range(len(edges)):
                    if n + 1 < len(edges):
                        if self.g.has_edge(edges[n], edges[n + 1]):
                            self.g.remove_edge(edges[n], edges[n + 1])
                        elif self.g.has_edge(edges[n + 1], edges[n]):
                            self.g.remove_edge(edges[n + 1], edges[n])
                        self.g.add_edge(edges[n], edges[n + 1], color='red')
                    else:
                        if self.g.has_edge(edges[n], edges[0]):
                            self.g.remove_edge(edges[n], edges[0])
                        elif self.g.has_edge(edges[0], edges[n]):
                            self.g.remove_edge(edges[0], edges[n])
                        self.g.add_edge(edges[n], edges[0], color='red')

        colors = nx.get_edge_attributes(self.g, 'color').values()
        nx.draw_kamada_kawai(self.g, edge_color=colors, with_labels=True)
        self.w.xolst.draw()
