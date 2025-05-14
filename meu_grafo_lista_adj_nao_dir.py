from operator import truediv

from bibgrafo.grafo_lista_adj_nao_dir import GrafoListaAdjacenciaNaoDirecionado
from bibgrafo.grafo_errors import *


class MeuGrafo(GrafoListaAdjacenciaNaoDirecionado):

    def vertices_nao_adjacentes(self):
        '''
        Provê um conjunto de vértices não adjacentes no grafo.
        O conjunto terá o seguinte formato: {X-Z, X-W, ...}
        Onde X, Z e W são vértices no grafo que não tem uma aresta entre eles.
        :return: Um objeto do tipo set que contém os pares de vértices não adjacentes
        '''

        adjacentes = []
        todasrelacoes = []

        for verticeA in self.vertices:
            for verticeB in self.vertices:
                if verticeA.rotulo != verticeB.rotulo:
                    #print(verticeA.rotulo,verticeB.rotulo)
                    if verticeA.rotulo < verticeB.rotulo:
                        todasrelacoes.append(verticeA.rotulo + "-" + verticeB.rotulo)
                    else:
                        todasrelacoes.append(verticeB.rotulo + "-" + verticeA.rotulo)
        for aresta in self.arestas.values():

            if aresta.v1.rotulo < aresta.v2.rotulo:
                adjacentes.append(aresta.v1.rotulo + "-" + aresta.v2.rotulo)
            else:
                adjacentes.append(aresta.v2.rotulo + "-" + aresta.v1.rotulo)

        #print(sorted(todasrelacoes))
        #print(sorted(adjacentes))
        todasrelacoes = set(todasrelacoes)
        adjacentes = set(adjacentes)
        naoadjacentes = todasrelacoes - adjacentes
        #print(naoadjacentes)
        return naoadjacentes




    def ha_laco(self):
        '''
        Verifica se existe algum laço no grafo.
        :return: Um valor booleano que indica se existe algum laço.
        '''
        for aresta in self.arestas.values():
            if aresta.v1 == aresta.v2:
                return True
        return False


    def grau(self, V=''):
        '''
        Provê o grau do vértice passado como parâmetro
        :param V: O rótulo do vértice a ser analisado
        :return: Um valor inteiro que indica o grau do vértice
        :raises: VerticeInvalidoError se o vértice não existe no grafo
        '''
        if self.existe_rotulo_vertice(V) == False:
            raise VerticeInvalidoError
        grau = 0
        for aresta in self.arestas.values():
            if aresta.v1.rotulo == V:
                grau = grau + 1
            if aresta.v2.rotulo == V:
                grau = grau + 1
        return grau
    def ha_paralelas(self):
        '''
        Verifica se há arestas paralelas no grafo
        :return: Um valor booleano que indica se existem arestas paralelas no grafo.
        '''
        arestas = []

        for aresta in self.arestas.values():
            if aresta.v1.rotulo < aresta.v2.rotulo:
                atual = aresta.v1.rotulo+aresta.v2.rotulo
            else:
                atual = aresta.v1.rotulo+aresta.v2.rotulo
            if atual in arestas:
                return True
            else:
                arestas.append(atual)
        return False


    def arestas_sobre_vertice(self, V):
        '''
        Provê uma lista que contém os rótulos das arestas que incidem sobre o vértice passado como parâmetro
        :param V: Um string com o rótulo do vértice a ser analisado
        :return: Uma lista os rótulos das arestas que incidem sobre o vértice
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''
        arestas = set()
        if not self.existe_rotulo_vertice(V):
            raise VerticeInvalidoError
        for aresta in self.arestas.values():
            if aresta.v1.rotulo == V or aresta.v2.rotulo == V:
                arestas.add(aresta.rotulo)
        return arestas

    def eh_completo(self):
        '''
        Verifica se o grafo é completo.
        :return: Um valor booleano que indica se o grafo é completo
        '''

        primoteste = False
        for vertice in self.vertices:
            grau = self.grau(vertice.rotulo)
            if primoteste:
                if grau != antegrau:
                    return False
            else:
                primoteste = True
            antegrau = grau
        if self.ha_laco():
            return False
        if self.ha_paralelas():
            return False
        if self.vertices_nao_adjacentes():
            return False
        return True

    def bfs(self, V=''):

        grafo = MeuGrafo()
        arestas_nao_visitadas_restantes = len(self.arestas)
        vertice_visitado = []
        inicio = None

        for aresta in self.arestas:
            break


        print(arestas_nao_visitadas_restantes)

        return arestas_nao_visitadas_restantes
