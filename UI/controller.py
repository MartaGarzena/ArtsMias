import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handleAnalizzaOggetti(self, e):
        self._model.buildGraph()
        self._view.txt_result.controls.append(ft.Text(f"grafo creato, contiene {self._model.getNumNodes()} nodi e {self._model.getNumEdges()} archi"))
        self._view.update_page()

    def handleCompConnessa(self,e):
        txtInput=self._view._txtIdOggetto.value

        if txtInput == "":
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(
                ft.Text(f"Inserici qualcosa di valido", color="red"))
            self._view.update_page()

        try:
            idIN=int(txtInput)
        except ValueError:
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(
                ft.Text(f"non hai inserito un numero", color="red"))
            self._view.update_page()

        if not self._model.hasNode(idIN):
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(
                ft.Text(f"id non corrisponde a nulla", color="red"))
            self._view.update_page()

        sizeInfoConeessa =self._model.getInfoConnessa(idIN)
        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(
            ft.Text(f"La componente connessa che contiene il nodo {self._model.getObjFromId(idIN)} ha dimensione {self._model.getInfoConnessa(idIN)}", color="blue"))
        self._view.update_page()
