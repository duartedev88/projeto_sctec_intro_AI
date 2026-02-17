from __future__ import annotations

from pathlib import Path
from typing import Dict

import pandas as pd


DATA_DIR = Path(__file__).resolve().parents[1] / "data"


def carregar_csvs_da_pasta_data() -> Dict[str, pd.DataFrame]:
    # Carrega todos os CSVs da pasta data e devolve um dict {nome_arquivo: DataFrame}.
    if not DATA_DIR.exists():
        raise FileNotFoundError(f"Pasta de dados nao encontrada: {DATA_DIR}")

    csvs = sorted(DATA_DIR.glob("*.csv"))
    if not csvs:
        raise FileNotFoundError(f"Nenhum CSV encontrado em: {DATA_DIR}")

    return {arquivo.stem: pd.read_csv(arquivo) for arquivo in csvs}


def carregar_ncr_ride_bookings() -> pd.DataFrame:
    # Carrega o arquivo ncr_ride_bookings.csv da pasta data.
    arquivo = DATA_DIR / "ncr_ride_bookings.csv"
    if not arquivo.exists():
        raise FileNotFoundError(f"Arquivo nao encontrado: {arquivo}")
    return pd.read_csv(arquivo)


# Executa o bloco abaixo apenas quando o arquivo e executado como script,
# nao quando e importado.
if __name__ == "__main__":
    pd.set_option("display.max_columns", None)
    pd.set_option("display.width", None)
    datasets = carregar_csvs_da_pasta_data()
    for nome, df in datasets.items():
        print(f"{nome}: {df.shape} colunas={len(df.columns)}")
        print(df.head(5))
