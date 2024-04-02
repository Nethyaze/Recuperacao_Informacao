import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
nltk.download('punkt')
from Coletor import Coletor

class Indexador:
    def __init__(self, coletor):
        self.coletor = coletor
        self.stop_words = set(stopwords.words('portuguese'))
        self.inverted_index = {}

    def inverted_index_generator(self):
        for dado in self.coletor.dados_coletados:
            for tag, textos in dado.items():
                if tag != 'url':
                    for texto in textos:
                        palavras = texto.split()
                        for palavra in palavras:
                            palavra = palavra.lower()
                            if palavra not in self.inverted_index:
                                self.inverted_index[palavra] = set()
                            self.inverted_index[palavra].add(dado['url'])