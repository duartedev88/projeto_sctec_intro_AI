from __future__ import annotations

from pathlib import Path  # Caminhos de arquivo portaveis
from typing import Dict  # Tipagem para dicionarios

import pandas as pd  # Leitura de arquivos CSV


DATA_DIR = Path(__file__).resolve().parents[1] / "data"  # Pasta de dados do projeto


def carregar_csvs_da_pasta_data() -> Dict[str, pd.DataFrame]:
    # Carrega todos os CSVs da pasta data e devolve um dict {nome_arquivo: DataFrame}.
    if not DATA_DIR.exists():
        # Garante erro claro se a pasta data nao existir
        raise FileNotFoundError(f"Pasta de dados nao encontrada: {DATA_DIR}")

    # Lista todos os arquivos .csv da pasta
    csvs = sorted(DATA_DIR.glob("*.csv"))
    if not csvs:
        # Garante erro claro se nao houver CSV
        raise FileNotFoundError(f"Nenhum CSV encontrado em: {DATA_DIR}")

    # Le cada CSV e retorna em um dicionario {nome_do_arquivo: DataFrame}
    return {arquivo.stem: pd.read_csv(arquivo) for arquivo in csvs}


def carregar_ncr_ride_bookings() -> pd.DataFrame:
    # Carrega o arquivo ncr_ride_bookings.csv da pasta data.
    arquivo = DATA_DIR / "ncr_ride_bookings.csv"
    if not arquivo.exists():
        # Erro claro se o arquivo nao estiver presente
        raise FileNotFoundError(f"Arquivo nao encontrado: {arquivo}")
    # Le o CSV e retorna o DataFrame
    return pd.read_csv(arquivo)


# Executa o bloco abaixo apenas quando o arquivo e executado como script,
# nao quando e importado.
if __name__ == "__main__":
    # Ajusta exibicao para ver todas as colunas no terminal
    pd.set_option("display.max_columns", None)
    pd.set_option("display.width", None)
    # Carrega todos os datasets e imprime um resumo rapido
    datasets = carregar_csvs_da_pasta_data()
    for nome, df in datasets.items():
        print(f"{nome}: {df.shape} colunas={len(df.columns)}")
        print(df.head(5))
