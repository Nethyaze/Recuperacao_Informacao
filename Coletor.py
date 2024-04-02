from bs4 import BeautifulSoup
import json
from urllib.parse import urljoin
from Url import Url

class Coletor:
    def __init__(self):
        self.urls_visitadas = set()
        self.dados_coletados = []

    def coletar_urls(self, url_inicial, profundidade=1, tags=['h1', 'h2', 'p']):
        if profundidade == 0 or url_inicial in self.urls_visitadas:
            return

        url_objeto = Url(url_inicial)
        html = url_objeto.buscar_html()
        if html:
            self.urls_visitadas.add(url_inicial)
            soup = BeautifulSoup(html, 'html.parser')
            tags_a = soup.find_all('a', href=True)
            for tag_a in tags_a:
                href = tag_a['href']
                href_absoluto = urljoin(url_inicial, href)
                dados_url = {'url': href_absoluto}
                for tag in tags:
                    tags_texto = soup.find_all(tag)
                    dados_url[tag] = [tag_texto.get_text(strip=True) for tag_texto in tags_texto]
                self.dados_coletados.append(dados_url)
                self.coletar_urls(href_absoluto, profundidade - 1)

    def salvar_dados_json(self, nome_arquivo):
        with open(nome_arquivo, 'w') as arquivo:
            json.dump(self.dados_coletados, arquivo, indent=4)


