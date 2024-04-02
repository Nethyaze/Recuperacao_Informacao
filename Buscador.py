from indexador import Indexador
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
nltk.download('punkt')

class Buscador:
    def __init__(self, indexador):
        self.indexador = indexador

    def buscar(self, termo):
        termo = termo.lower()
        if termo in self.indexador.inverted_index:
            return self.indexador.inverted_index[termo]
        else:
            return "Nenhum resultado encontrado para o termo de busca."

    def buscar_todos_termos(self, consulta):
        tokens_consulta = nltk.word_tokenize(consulta)
        links_relevantes = set()
        for token in tokens_consulta:
            if token in self.indexador.inverted_index:
                if not links_relevantes:
                    links_relevantes = set(self.indexador.inverted_index[token])
                else:
                    links_relevantes.intersection_update(self.indexador.inverted_index[token])
        return links_relevantes if links_relevantes else "Nenhum resultado encontrado para a consulta."
