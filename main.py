from pathlib import Path  # Caminhos de arquivo de forma portavel

import pandas as pd  # Leitura e manipulacao de dados tabulares

from srs.limpeza_dados import limpeza_dados  # Aplica as regras de limpeza
from srs.visualizacao import (
    grafico_corridas_horas,  # Grafico de corridas por hora
    grafico_dia_semana,  # Grafico de corridas por dia da semana
    grafico_distancia_preco,  # Grafico de distancia x preco
)

if __name__ == "__main__":  # Garante execucao apenas quando rodar este arquivo
    # Monta o caminho absoluto do CSV dentro da pasta data
    caminho = Path(__file__).resolve().parent / "data" / "ncr_ride_bookings.csv"
    # Le o CSV bruto para um DataFrame
    df_bruto = pd.read_csv(caminho)
    # Aplica as regras de limpeza e padronizacao
    df_limpo = limpeza_dados(df_bruto)

    # Gera os graficos a partir dos dados limpos
    grafico_corridas_horas(df_limpo)
    grafico_dia_semana(df_limpo)
    grafico_distancia_preco(df_limpo)
