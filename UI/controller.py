import flet as ft
from UI.view import View
from model.model import Model

class Controller:
    def __init__(self, view: View, model: Model):
        self._view = view
        self._model = model

    def handle_crea_grafo(self, e):
        """ Handler per gestire creazione del grafo """""
        self._view.txt_out_squadre.controls.clear()

        self._model.build_graph(self._view.dd_anno.value)

        self._view.txt_out_squadre.controls.append(ft.Text(f'Numero di squadre: {len(self._model.G.nodes())}'))

        for nodo in self._model.G.nodes():
            self._view.txt_out_squadre.controls.append(ft.Text(f'{nodo.team_code} ({nodo.name})'))
            self._view.dd_squadra.options.append(ft.dropdown.Option(text=f'{nodo.team_code} ({nodo.name})', key= nodo.id))

        self._view.update()

    def handle_dettagli(self, e):
        """ Handler per gestire i dettagli """""
        for u, v, w in self._model.G.edges(data=True):
            if str(u.id) == self._view.dd_squadra.value:
                self._view.txt_risultato.controls.append(ft.Text(f'{v.team_code} ({v.name}) -> peso {w['weight']}'))
            elif str(v.id) == self._view.dd_squadra.value:
                self._view.txt_risultato.controls.append(ft.Text(f'{u.team_code} ({u.name}) -> peso {w['weight']}'))

        self._view.update()

    def handle_percorso(self, e):
        """ Handler per gestire il problema ricorsivo di ricerca del percorso """""


    """ Altri possibili metodi per gestire di dd_anno """""
    def popola_dd(self):

        for year in self._model.get_year():
            self._view.dd_anno.options.append(ft.dropdown.Option(str(year)))

        self._view.update()