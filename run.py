# -*- coding: utf-8 -*-
import os
import csv
import json
from uuid import uuid4
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor,as_completed

def get_time_now():
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')

def download_file(row):
    file_name = f"folhacet{row['year']}"

    ROOT_DIR = os.path.realpath(os.path.dirname(__file__))
    CSV_FILE = f'{file_name}.csv'

    if not os.path.isfile(f'{ROOT_DIR}/{CSV_FILE}'):

        print(f"{get_time_now()} downloading file {row['url']}")
        with requests.get(row['url']) as r:
            with open(f'{ROOT_DIR}/{CSV_FILE}', 'wb') as f:
                f.write(r.content)
                f.close()
                print(f"{get_time_now()} download Ok {CSV_FILE}")

    with open(f'{ROOT_DIR}/{CSV_FILE}', 
            encoding='utf-8', errors='ignore') as f:

        reader = csv.reader(f, delimiter=';')
        first = True

        for row in reader:
            if not first:
                empresa = row[0]
                mes = row[1]
                ano = row[2]
                nome = row[3]
                cargo = row[4]
                lotacao = row[5]
                admissao = row[6]
                nascimento = row[7]
                vencimentos = row[8].strip()
                encargos = row[9].strip()
                beneficios = row[10].strip()
                outras_remuneracoes = row[11].strip()
                vinculo = row[12]
                detalhe_vinculo = row[13]
                liminar = row[14]
                arquivo_id = row[15]

                dict_bf = { 
                    'empresa': empresa, 
                    'mes': mes, 
                    'ano': ano, 
                    'nome': nome, 
                    'cargo': cargo, 
                    'lotacao': lotacao, 
                    'admissao': admissao, 
                    'nascimento': nascimento, 
                    'vencimentos': vencimentos, 
                    'encargos': encargos, 
                    'beneficios': beneficios, 
                    'outras_remuneracoes': outras_remuneracoes, 
                    'vinculo': vinculo, 
                    'detalhe_vinculo': detalhe_vinculo, 
                    'liminar': liminar, 
                    'arquivo_id': arquivo_id 
                }
                
                # hashing json file name with uuid
                hash = uuid4().hex
                
                file_json = f'{ROOT_DIR}/data/{hash}.json'.lower()

                # save file 
                with open(file_json, mode="w") as f:
                    f.write(json.dumps(dict_bf, indent=4))

                print(f'{get_time_now()} [ Ok ] {hash} {nome}')

            else:
                first = not first

    return f'{CSV_FILE}'

#===============================================================================
if __name__ == '__main__':
    print(f"{get_time_now()} Starting... ")

    URL_CET_PAGTOS = 'http://dados.prefeitura.sp.gov.br'
    URL_CET_PAGTOS = f'{URL_CET_PAGTOS}/dataset/folha-de-pagamento-cet'

    yearOfPayroll = [ '2020' ] # just one
    links = []

    print(f"{get_time_now()} yearOfPayroll {yearOfPayroll}")

    # getting page content
    result = requests.get(URL_CET_PAGTOS)

    # parsing
    soup = BeautifulSoup(result.text, features='html.parser')

    for el in soup.select('ul.resource-list li.resource-item'):
        year = el.find('a', { 'class': 'heading'})['title'][-4:]
        url = el.find('a', { 'class': 'resource-url-analytics'})['href']

        if year in yearOfPayroll and '.csv' in url:
            links.append({ 'year': year, 'url': url})

    # threading in python to run faster (asynchronous)
    with ThreadPoolExecutor(max_workers=3) as executor:
        for thread in as_completed({ 
                executor.submit(download_file, row): row for row in links 
            }):
            try:
                thread.result()
            except Exception as e:
                print(f"{get_time_now()} ERROR {e}")

    exit(0)