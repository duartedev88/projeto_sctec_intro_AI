from __future__ import annotations

import matplotlib.pyplot as plt
import pandas as pd

from srs.limpeza_dados import limpeza_dados


def _coluna_por_nome(df, nome):
    # Encontra o nome real da coluna com comparacao case-insensitive.
    nome_normalizado = nome.strip().lower()
    for coluna in df.columns:
        if coluna.strip().lower() == nome_normalizado:
            return coluna
    return None


def _validar_colunas(df, colunas):
    faltando = [col for col in colunas if col not in df.columns]
    if faltando:
        raise ValueError(f"Colunas ausentes no DataFrame: {', '.join(faltando)}")


def grafico_corridas_horas(df, coluna_hora="hora", show=True):
    # Gera grafico de contagem de corridas por hora.
    df = limpeza_dados(df)
    _validar_colunas(df, [coluna_hora])

    contagem = df[coluna_hora].value_counts().sort_index()
    fig, ax = plt.subplots()
    contagem.plot(kind="bar", ax=ax, color="#2E7D32")
    ax.set_title("Corridas por hora")
    ax.set_xlabel("Hora")
    ax.set_ylabel("Quantidade")
    fig.tight_layout()

    if show:
        plt.show()
    return fig, ax


def grafico_dia_semana(df, coluna_dia="dia_semana", show=True):
    # Gera grafico de contagem de corridas por dia da semana.
    df = limpeza_dados(df)
    _validar_colunas(df, [coluna_dia])

    ordem = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
    ]
    contagem = df[coluna_dia].value_counts().reindex(ordem)
    fig, ax = plt.subplots()
    contagem.plot(kind="bar", ax=ax, color="#1565C0")
    ax.set_title("Corridas por dia da semana")
    ax.set_xlabel("Dia da semana")
    ax.set_ylabel("Quantidade")
    fig.tight_layout()

    if show:
        plt.show()
    return fig, ax


def grafico_distancia_preco(
    df,
    coluna_distancia="ride distance",
    coluna_preco="booking value",
    show=True,
):
    # Gera grafico de dispersao entre distancia e preco.
    coluna_distancia = _coluna_por_nome(df, coluna_distancia)
    coluna_preco = _coluna_por_nome(df, coluna_preco)
    if not coluna_distancia or not coluna_preco:
        faltando = []
        if not coluna_distancia:
            faltando.append("ride distance")
        if not coluna_preco:
            faltando.append("booking value")
        raise ValueError(f"Colunas ausentes no DataFrame: {', '.join(faltando)}")

    distancia = pd.to_numeric(df[coluna_distancia], errors="coerce")
    preco = pd.to_numeric(df[coluna_preco], errors="coerce")
    dados = pd.DataFrame({"distancia": distancia, "preco": preco}).dropna()

    fig, ax = plt.subplots()
    ax.scatter(dados["distancia"], dados["preco"], alpha=0.6, color="#EF6C00")
    ax.set_title("Distancia vs. preco")
    ax.set_xlabel("Distancia")
    ax.set_ylabel("Preco")
    fig.tight_layout()

    if show:
        plt.show()
    return fig, ax
