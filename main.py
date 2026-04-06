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

    dados_extraidos = []

    for livro in livros_html:
        titulo = livro.h3.a['title']
        preco = livro.find('p', class_='price_color').text
        dados_extraidos.append({
            "Título": titulo,
            "Preço": preco
        })
    print (dados_extraidos)

    relatorio_livros = open('relatorio_livros.csv', mode='w', newline='', encoding='utf-8')
    fieldnames = ["Título", "Preço"]
    
    writer = csv.DictWriter(relatorio_livros, fieldnames=fieldnames)

    writer.writeheader()
    for livro in dados_extraidos:
        writer.writerow(livro)
    
    print("Relatório CSV gerado com sucesso!")

if __name__ == "__main__":
    main()