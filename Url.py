import requests
from urllib.parse import urljoin

class Url:
    def __init__(self, url):
        self.url = url

    def buscar_html(self):
        try:
            # Requisição GET para obter o HTML da página
            resposta = requests.get(self.url, allow_redirects=True)
            # Verifica se houve redirecionamento
            if resposta.history:
                print(f"Redirecionamento detectado para a URL: {self.url}")
                # Pega a URL final após redirecionamento
                self.url = resposta.url
            # Verifica se a solicitação foi bem-sucedida (código de status 200)
            if resposta.status_code == 200:
                return resposta.text
            else:
                print(f"Falha ao buscar o HTML de {self.url}. Código do erro: {resposta.status_code}")
                return None
        # Tratamento de exceção do GET
        except requests.exceptions.RequestException as erro:
            print(f"Ocorreu um erro ao buscar o HTML de {self.url}: {str(erro)}")
            return None
