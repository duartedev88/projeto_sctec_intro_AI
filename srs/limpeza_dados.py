import pandas as pd  # Manipulacao de dados tabulares


def _coluna_por_nome(df, nome):
    # Encontra o nome real da coluna ignorando maiusculas/minusculas.
    nome_normalizado = nome.strip().lower()
    for coluna in df.columns:
        if coluna.strip().lower() == nome_normalizado:
            return coluna
    return None


def _limpar_date(df):
    # Converte data/hora para datetime, cria hora e dia da semana.
    coluna_date = _coluna_por_nome(df, "date")
    coluna_time = _coluna_por_nome(df, "time")
    if not coluna_date:
        return df

    if coluna_time:
        # Combina colunas de data e hora quando ambas existem
        serie = df[coluna_date].astype(str) + " " + df[coluna_time].astype(str)
        df['date'] = pd.to_datetime(serie, errors="coerce")
    else:
        # Converte a coluna de data isolada para datetime
        df['date'] = pd.to_datetime(df[coluna_date], errors="coerce")
    # Cria coluna de hora (0-23)
    df['hora'] = df['date'].dt.hour
    # Cria coluna com o nome do dia da semana
    df['dia_semana'] = df['date'].dt.day_name()
    # Remove linhas com datas invalidas
    return df.dropna(subset=['date'])


def _limpar_payment_method(df):
    # Remove nulos e padroniza o metodo de pagamento.
    coluna_payment = _coluna_por_nome(df, "payment method")
    if not coluna_payment:
        return df

    # Remove linhas sem metodo de pagamento
    df = df.dropna(subset=[coluna_payment])
    # Normaliza valores para comparacão
    normalizado = (
        df[coluna_payment]
        .astype(str)
        .str.strip()
        .str.lower()
    )
    # Converte variacões de nomes para um conjunto padrão
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
    # Aplica o mapeamento e preserva valores desconhecidos
    df[coluna_payment] = normalizado.map(mapeamento).fillna(normalizado)
    return df


def _limpar_cancelled_rides_by_driver(df):
    # Normaliza cancelamentos do motorista para 0/1.
    coluna_cancel = _coluna_por_nome(df, "cancelled rides by driver")
    if not coluna_cancel:
        return df

    # Mapeia representacões comuns para 0/1
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
    # Normaliza texto para facilitar o mapeamento
    normalizado = (
        df[coluna_cancel]
        .astype(str)
        .str.strip()
        .str.lower()
    )
    # Aplica mapeamento, preenche nulos e converte para inteiro
    df[coluna_cancel] = normalizado.map(mapeamento_cancelamento)
    df[coluna_cancel] = df[coluna_cancel].fillna(0).astype(int)
    return df

def limpeza_dados(df):
    # Aplica todas as etapas de limpeza em sequencia.
    df = df.copy()
    df = _limpar_date(df)
    df = _limpar_payment_method(df)
    df = _limpar_cancelled_rides_by_driver(df)
    return df
