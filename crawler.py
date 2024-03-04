import csv
import json
import requests
from bs4 import BeautifulSoup

lista_de_vagas = []
linkedin_url = "https://www.linkedin.com/jobs/search"
response = requests.get(
    linkedin_url,
    params={
        "keywords": "Estagio Junior",
        "location": "Brazil",
        "trk": "guest_homepage-basic_guest_nav_menu_jobs"
    })

contexto = BeautifulSoup(response.content, 'html.parser')

seleciona_vagas = contexto.select(".jobs-search__results-list li")
for vaga in seleciona_vagas:
    titulo_elementos = vaga.select(".base-search-card__title")
    empresa_elementos = vaga.select(".base-search-card__subtitle")
    localidade_elementos = vaga.select(".job-search-card__location")
    links = vaga.select(".base-card__full-link")
    time_element = vaga.find("time")

    if titulo_elementos and empresa_elementos and localidade_elementos and links and time_element:
        titulo = titulo_elementos[0].text.strip()
        empresa = empresa_elementos[0].text.strip()
        localidade = localidade_elementos[0].text.strip()

        if links:
            link = links[0].get("href")
        else:
            link = "Link não disponível"

        data_publicacao = time_element.get("datetime")

        print(f"Vaga: {titulo}")
        print(f"Empresa: {empresa}")
        print(f"Localidade: {localidade}")
        print(f"Data de publicação: {data_publicacao}")
        print(f"Link da vaga: {link}")
        print()

        info = {
            "vaga": titulo,
            "empresa": empresa,
            "localidade": localidade,
            "data_publicacao": data_publicacao,
            "link": link
        }

        lista_de_vagas.append(info)

with open("vagas.json", "w", encoding="utf-8") as arquivo_json:
    arquivo_json.write(json.dumps(
        lista_de_vagas, ensure_ascii=False, indent=4))

with open('vagas.csv', mode='w', encoding="utf-8") as arquivo_csv:
    cabecalho = ['vaga', 'empresa', 'localidade', "data_publicacao", "link"]
    gerador_csv = csv.DictWriter(arquivo_csv, fieldnames=cabecalho)
    gerador_csv.writeheader()
    gerador_csv.writerows(lista_de_vagas)
