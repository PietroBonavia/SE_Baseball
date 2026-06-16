import networkx as nx
from database.dao import DAO

class Model:
    def __init__(self):
        self.G = nx.Graph()

    def get_year(self):
        return DAO.get_year()

    def build_graph(self, anno):
        nodi = DAO.get_squadre_salario(anno)
        self.G.add_nodes_from(nodi)

        for nodo1 in nodi:
            for nodo2 in nodi:
                if nodo1 != nodo2 and (nodo1,nodo2) not in self.G and (nodo2,nodo1) not in self.G:
                        self.G.add_edge(nodo1, nodo2, weight= nodo1.tot_salari + nodo2.tot_salari)