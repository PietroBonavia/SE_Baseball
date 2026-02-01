import flet as ft
from UI.view import View
from model.model import Model

class Controller:
    def __init__(self, view: View, model: Model):
        self._view = view
        self._model = model

    def handle_crea_grafo(self, e):
        """ Handler per gestire creazione del grafo """""
        self._model.crea_grafo(self._view.dd_anno.value)

        self._view.update()



    def handle_dettagli(self, e):
        """ Handler per gestire i dettagli """""
        self._view.txt_risultato.clean()
        mappa = self._model.mappa(self._view.dd_anno.value)

        valore = self._view.dd_squadra.value[:3]
        nodo = mappa[valore]

        lista = []
        vicini = self._model.dettagli(nodo)
        for vicino in vicini:
            for u,v, w in self._model.G.edges(data=True):
                if (vicino == u and nodo == v) or (vicino == v and nodo == u):
                    lista.append((vicino, w['weight']))


        lista.sort(key=lambda x: x[1], reverse=True)

        for elemento in lista:
            self._view.txt_risultato.controls.append(ft.Text(f'{elemento[0].team_code}({elemento[0].name}) - peso {elemento[1]}'))

        self._view.update()


    def handle_percorso(self, e):
        """ Handler per gestire il problema ricorsivo di ricerca del percorso """""
        # TODO

    """ Altri possibili metodi per gestire di dd_anno """""
    def popola_anni(self):
        anni = self._model.get_anni()
        for anno in anni:
            self._view.dd_anno.options.append(ft.dropdown.Option(str(anno)))



    def popola_squadre(self, e):
        self._view.txt_out_squadre.clean()
        self._view.dd_squadra.options.clear()

        squadre = self._model.get_squadre(self._view.dd_anno.value)

        self._view.txt_out_squadre.controls.append(ft.Text(f'Numero di squadre: {len(squadre)}'))

        for squadra in squadre:
            self._view.txt_out_squadre.controls.append(ft.Text(f'{squadra.team_code}({squadra.name})'))
            self._view.dd_squadra.options.append(ft.dropdown.Option(f'{squadra.team_code}({squadra.name})'))



        self._view.update()



