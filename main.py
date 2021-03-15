import time
from datetime import datetime
import requests
from selenium import webdriver as wd
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup as bs
import pandas as pd

# Usar Beautiful Soup pra pegar o html e montar listas

produto = input("Nome do produto pra pesquisar: ")
url = 'https://www.amazon.com.br/s?k={}'.format(produto)
print('acessando {}'.format(url))

page = requests.get(url)
soup = bs(page.content, 'html.parser')

lista_titulos = soup.select(".a-link-normal.a-text-normal .a-text-normal")[:10]
lista_precos = soup.select(".a-price .a-offscreen")[:10]
titulos = [titulo.get_text() for titulo in lista_titulos]
precos = [preco.get_text().replace('\xa0','') for preco in lista_precos]

print('Tamanho dos arrays: {}, {}'.format(len(titulos), len(precos)))
print(titulos)
print(precos)
# Usar Pandas pra montar o dataframe

tabela_resultados = pd.DataFrame({
    'nome': titulos,
    'preco': precos 
})

print(tabela_resultados)
tabela_resultados.to_csv('resultados.csv')

# Fechando conexões