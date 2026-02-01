import networkx as nx

from database.dao import DAO


class Model:
    def __init__(self):
        self.squadre = []

        self.G = nx.Graph()
        self.map = {}

    def mappa(self,anno):
        self.squadre = DAO.read_squadre(anno)
        for squadra in self.squadre:
            self.map[squadra.team_code] = squadra

        return self.map

    def get_anni(self):
        return DAO.read_anni()

    def get_squadre(self, anno):

        return DAO.read_squadre(anno)

    def crea_grafo(self, anno):

        self.squadre = DAO.read_squadre(anno)
        stipendi = DAO.read_stipendi(anno)

        self.G.add_nodes_from(self.squadre)

        for s1 in self.squadre:
            stipendio1 = stipendi[s1.team_code]
            for s2 in self.squadre:
                stipendio2 = stipendi[s2.team_code]
                if s1!= s2:
                    self.G.add_edge(s1, s2, weight = stipendio1 + stipendio2)



    def dettagli(self, squadra):

        return list(self.G.neighbors(squadra))






