import requests
from bs4 import BeautifulSoup
import csv

def main():
    print("Iniciando o web scraping...")
    url = "http://books.toscrape.com/"
    resposta = requests.get(url)

    if resposta.status_code != 200:
        print(f"Erro ao acessar o site. Status code: {resposta.status_code}")
        exit()
    else:
        print("Conexão bem-sucedida!")

    soup = BeautifulSoup(resposta.text, 'html.parser')
    title = soup.title
    print(title)
    
    livros_html = soup.find_all('article', class_='product_pod')
    print(len(livros_html))

if __name__ == "__main__":
    main()