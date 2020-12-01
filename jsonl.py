import json

'''Cria arquivo e insere os dados no formato jsonl'''
def create_jsonl_file(array):
    with open('data.jsonl', 'w', encoding='utf8') as f:
        for i in range(len(array)):
            for j in range(len(array[i])):
                item = array[i][j]
                f.write(json.dumps(item, ensure_ascii=False) + '\n')