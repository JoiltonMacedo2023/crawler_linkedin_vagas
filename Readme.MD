# Web Scraping de Vagas de Emprego no LinkedIn

Este script Python realiza web scraping das vagas de emprego no LinkedIn com base em palavras-chave e localização especificadas. Ele extrai informações sobre as vagas encontradas, como título, empresa, localização, data de publicação e link para a vaga.

## Requisitos

Python 3.x

Bibliotecas: requests, BeautifulSoup

## Como usar

Clone este repositório:

git clone https://github.com/seu-usuario/nome-do-repositorio.git

Instale as dependências necessárias:

pip install -r requirements.txt

Execute o script:

python scraper.py

Os resultados serão salvos em dois arquivos:

vagas.json: arquivo JSON contendo as informações das vagas.

vagas.csv: arquivo CSV contendo as informações das vagas.

## Personalização

Você pode personalizar a pesquisa editando as variáveis keywords e location no arquivo scraper.py. Ajuste essas variáveis para refletir as palavras-chave e a localização desejadas para a busca de vagas.

linkedin_url = "https://www.linkedin.com/jobs/search"
response = requests.get(
linkedin_url,
params={
"keywords": "Python Junior", # Palavras-chave para a busca
"location": "Brazil", # Localização para a busca
"trk": "guest_homepage-basic_guest_nav_menu_jobs"
})

## Observações:

Este script foi desenvolvido para fins educacionais e de aprendizado.

O uso excessivo ou abusivo do web scraping pode violar os termos de serviço de alguns sites, incluindo o LinkedIn.
