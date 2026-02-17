from pathlib import Path

import pandas as pd

from srs.limpeza_dados import limpeza_dados
from srs.visualizacao import (
    grafico_corridas_horas,
    grafico_dia_semana,
    grafico_distancia_preco,
)

if __name__ == "__main__":
    caminho = Path(__file__).resolve().parent / "data" / "ncr_ride_bookings.csv"
    df_bruto = pd.read_csv(caminho)
    df_limpo = limpeza_dados(df_bruto)

    grafico_corridas_horas(df_limpo)
    grafico_dia_semana(df_limpo)
    grafico_distancia_preco(df_limpo)
