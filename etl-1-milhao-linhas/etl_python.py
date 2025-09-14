from csv import reader
from collections import defaultdict
import time

from pathlib import Path

PATH_TXT = "Projetos\etl-1-milhao-linhas\data\measurements.txt"

def processar_temperaturas(path_txt: Path):
    print ("Iniciando o processamento do arquivo.")

    start_time = time.time() # Tempo de início

    temperature_by_station = defaultdict(list)

    with open (path_txt, 'r', encoding='utf-8') as file:
        _reader = reader(file, delimiter=';')
        for row in _reader:
            station, temperature = str(row[0]), float(row[1])
            temperature_by_station[station].append(temperature)

    print("Dados carregados. Calculando estatísticas...")

    results = {}

    for station, temperature in temperature_by_station.items():
        min_temp = min(temperature)
        mean_temp = sum(temperature) / len(temperature)
        max_temp = max(temperature)
        results[station] = (min_temp, mean_temp, max_temp)

    print("Estatística calculada. Ordenando...")
    # Ordenando os resultados pelo nome da estação
    sorted_results = dict(sorted(results.items()))

    formatted_results = {station: f"{min_temp:.1f}/{mean_temp:.1f}/{max_temp:.1f}" for station, (min_temp, mean_temp, max_temp) in sorted_results.items()}

    end_time = time.time()
    print(f"Processamento concluído em {end_time - start_time:.2f} segundos.")

    return formatted_results

if __name__ == "__main__":
    PATH_TXT: Path = Path(PATH_TXT)
    resultados = processar_temperaturas(PATH_TXT)