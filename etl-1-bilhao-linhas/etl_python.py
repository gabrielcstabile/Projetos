from csv import reader
from collections import defaultdict
import time

from pathlib import Path

PATH_TXT = "Projetos\etl-1-bilhao-linhas\data\measurements.txt"

def processar_temperaturas(path_txt: Path):
    print ("Iniciando o processamento do arquivo.")

    start_time = time.time() # Tempo de início

    temperatura_por_estacao = defaultdict(list)

    with open (path_txt, 'r', encoding='utf-8') as file:
        _reader = reader(file, delimiter=';')
        for row in _reader:
            nome_da_estacao, temperatura = str(row[0]), float(row[1])
            temperatura_por_estacao[nome_da_estacao.append(temperatura)]

print("Dados carregados. Calculando estatísticas...")
