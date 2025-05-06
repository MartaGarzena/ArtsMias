import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):

        self._graph = nx.Graph()
        self._nodes = DAO.getAllNodes()

        self._idMap = {}
        for v in self._nodes:
            self._idMap[v.object_id] = v

    def buildGraph(self):

        self._graph.add_nodes_from(self._nodes)
        self.addEdge2()

    def addEdge1(self):
        for u in self._nodes:
            for v in self._nodes:
                peso = DAO.getPeso(u, v)
                if peso is not None:
                    self._graph.add_edge(u, v, weight=peso)

    def addEdge2(self):
        allEdges = DAO.getAllArchi(self._idMap)
        for edge in allEdges:
            self._graph.add_edge(edge.o1, edge.o2, weight=edge.peso)

    def getNumNodes(self):
        return len(self._graph.nodes)

    def getNumEdges(self):
        return len(self._graph.edges)

    def getIdMap(self):
        return self._idMap

    def getObjectFromId(self, id):
        return self._idMap[id]

    def getInfoConnessa(self, id):
        """indentifica la componente connessa che contiene id  e ne
        restituisce la dimensione"""
        source = self._idMap[id]

        #modo1: conto i successori
        succ=nx.dfs_successors(self._graph, source)
        #restituisce un dizionario con una lista di oggetti
        res=[]
        for s in succ:
            res.extend(s)
        print("Size conness: ", len(res))

        #modo 2: conto i predecessori
        pred=nx.dfs_predecessors(self._graph, source)
        #restituisce un dizionario con un solo valore per nodo
        print("Size predecessors: ", len(pred.values()))

        #modo3: conto i nodi deel'albero di visita
        disTree=nx.dfs_tree(self._graph, source)
        print("Size tree: ", len(disTree.nodes()))

        #metido4
        conn=nx.node_connected_component(self._graph, source)
        print("Size connected component: ", len(conn))

        return len(conn)
    def hasNode(self, id):
        return id in self._nodes #boolena

    def getObjFromId(self, id):
        return self._idMap[id]
