from selenium.webdriver.support.ui import Select

from selenium import webdriver

from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By

from bs4 import BeautifulSoup, UnicodeDammit
import requests

from dotenv import load_dotenv, find_dotenv
import os

load_dotenv('config.env')
driver_path = os.getenv('executable_path')

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options, executable_path=driver_path)

url = "http://www.buscacep.correios.com.br/sistemas/buscacep/buscaFaixaCEP.cfm"

def get_all_uf():
    try: 
        response = requests.get(url, allow_redirects=False)
        content = response.content
        html = BeautifulSoup(content, 'html.parser')

        options = html.find('select', class_="f1col")

        items = options.select('option[value]')
        values = [item.get('value') for item in items]
        values = values[1:]

        return values

    except:
        driver_close()
    
def submit_consulta_cep(option_value):
    try:
        driver.minimize_window()
        driver.get(url)

        Select(driver.find_element(By.TAG_NAME, 'select')).select_by_value(option_value)
        driver.find_element_by_xpath("//input[@value='Buscar']").submit()

    except:
        driver_close()        

def busca_faixa_cep(uf):
    localidade_duplicada =[] 
    faixa_cep = []
    while True:
        
        content = driver.page_source
        html_page = BeautifulSoup(content, 'html.parser')
        table = html_page.find_all('table')
        
        lista_td = []
        for e in table:
            td = e.find_all('td')
            td = [x.text.strip() for x in td]
            lista_td = td

        count = 0
        for i in range(len(lista_td)):
            count+=1
            if count >= 4:
                count = 0
                indice_inicial = i-3
                indice_final = i+1
                arr_aux = lista_td[indice_inicial:indice_final]
                
                uf = uf
                localidade = arr_aux[0]
                faixa_de_cep = [arr_aux[1]]
                situacao = [arr_aux[2]]
                tipo_de_faixa = [arr_aux[3]]
                               
                tamanho = len(faixa_cep)
                if tamanho >= 1 and faixa_cep[tamanho-1]['localidade'] == localidade:
                    
                    if faixa_cep[tamanho-1]['faixa_de_cep'] != faixa_de_cep:
                        faixa_cep[tamanho-1]['faixa_de_cep'].append(faixa_de_cep[0])
                    
                    if faixa_cep[tamanho-1]['situacao'] != situacao:
                        faixa_cep[tamanho-1]['situacao'].append(situacao[0])
                        
                    if faixa_cep[tamanho-1]['tipo_de_faixa'][0] != tipo_de_faixa:
                        faixa_cep[tamanho-1]['tipo_de_faixa'].append(tipo_de_faixa[0])
                    
                else:
                    json_object = {
                                    'id': 0,
                                    'UF': uf,
                                    'localidade' : localidade, 
                                    'faixa_de_cep' : faixa_de_cep, 
                                    'situacao' : situacao, 
                                    'tipo_de_faixa' : tipo_de_faixa
                                }
                    
                    faixa_cep.append(json_object)
                
        try:            
            driver.execute_script("javascript:document.Proxima.submit('Proxima')")
        except:
            break

    return faixa_cep

def id_generate(faixa_cep_dados):
    id = 1
    for i in range(len(faixa_cep_dados)):
        for j in range(len(faixa_cep_dados[i])):
            faixa_cep_dados[i][j]['id'] = id
            id+=1
    return faixa_cep_dados

def driver_close():
    driver.quit()