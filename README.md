# 🚀 Web Scraping Livraria

Este projeto é um script em Python criado para acessar dados do website de uma livraria online com dados estáticos, coletar informações de todos os livros da página principal e salvar em um relatório em formato CSV.

## 🛠️ Tecnologias Utilizadas

    * Python
    * Biblioteca Beautiful Soap (do módulo bs4)
    * Biblioteca Requests
    * Biblioteca csv (DictWriter)


## 📋 Funcionalidades e Implementação

    - Utilização da biblioteca requests para fazer a requisição GET a URL da livraria;
    
    - Verificação se a requisição à URL foi bem sucedida;
    
    - Utilização da biblioteca Beautiful Soap para extrair as informações do HTML (html parser);
    
    - Extração dos dados utilizando as funções de busca .findall() e .find();
    
    - Utilização do csv.DictWriter() para gravar os dados extraídos no arquivo relatorio_livros.csv.
    
