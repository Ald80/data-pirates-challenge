from busca_cep import *
from jsonl import create_jsonl_file

def main():
    lista_ufs = get_all_uf()
    faixa_cep_dados = []

    for i in range(len(lista_ufs)):
        uf = lista_ufs[i]
        submit_consulta_cep(uf)
        arr = busca_faixa_cep(uf)
        
        faixa_cep_dados.append(arr)
    
    faixa_cep_dados = id_generate(faixa_cep_dados)
    create_jsonl_file(faixa_cep_dados)
    driver_close()

main()