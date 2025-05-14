from bibgrafo.grafo_lista_adj_nao_dir import GrafoListaAdjacenciaNaoDirecionado
from bibgrafo.grafo_json import GrafoJSON
from meu_grafo_lista_adj_nao_dir import *

g_p = GrafoJSON.json_to_grafo('test_json/grafo_pb.json', MeuGrafo())

#print(g_p)

print(g_p.bfs())