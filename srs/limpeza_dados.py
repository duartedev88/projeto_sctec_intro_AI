from pathlib import Path

import pandas as pd


def _coluna_por_nome(df, nome):
    # Encontra o nome real da coluna com comparacao case-insensitive.
    nome_normalizado = nome.strip().lower()
    for coluna in df.columns:
        if coluna.strip().lower() == nome_normalizado:
            return coluna
    return None


def _limpar_date(df):
    # Converte date em datetime, cria hora/dia_semana e remove datas invalidas.
    coluna_date = _coluna_por_nome(df, "date")
    coluna_time = _coluna_por_nome(df, "time")
    if not coluna_date:
        return df

    if coluna_time:
        serie = df[coluna_date].astype(str) + " " + df[coluna_time].astype(str)
        df['date'] = pd.to_datetime(serie, errors="coerce")
    else:
        df['date'] = pd.to_datetime(df[coluna_date], errors="coerce")
    df['hora'] = df['date'].dt.hour
    df['dia_semana'] = df['date'].dt.day_name()
    return df.dropna(subset=['date'])


def _limpar_payment_method(df):
    # Remove nulos e normaliza valores de payment method.
    coluna_payment = _coluna_por_nome(df, "payment method")
    if not coluna_payment:
        return df

    df = df.dropna(subset=[coluna_payment])
    normalizado = (
        df[coluna_payment]
        .astype(str)
        .str.strip()
        .str.lower()
    )
    mapeamento = {
        'cash': 'cash',
        'dinheiro': 'cash',
        'card': 'card',
        'credit card': 'card',
        'debit card': 'card',
        'upi': 'upi',
        'wallet': 'wallet',
        'pix': 'pix',
    }
    df[coluna_payment] = normalizado.map(mapeamento).fillna(normalizado)
    return df


def _limpar_cancelled_rides_by_driver(df):
    # Normaliza cancelled rides by driver para 0/1 e preenche nulos.
    coluna_cancel = _coluna_por_nome(df, "cancelled rides by driver")
    if not coluna_cancel:
        return df

    mapeamento_cancelamento = {
        1: 1,
        0: 0,
        '1': 1,
        '0': 0,
        'yes': 1,
        'no': 0,
        'true': 1,
        'false': 0,
    }
    normalizado = (
        df[coluna_cancel]
        .astype(str)
        .str.strip()
        .str.lower()
    )
    df[coluna_cancel] = normalizado.map(mapeamento_cancelamento)
    df[coluna_cancel] = df[coluna_cancel].fillna(0).astype(int)
    return df

def limpeza_dados(df):
    # Aplica as funcoes de limpeza em etapas.
    df = df.copy()
    df = _limpar_date(df)
    df = _limpar_payment_method(df)
    df = _limpar_cancelled_rides_by_driver(df)
    return df

