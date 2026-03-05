# Projeto: Analise de corridas (NCR)

**Objetivo**
Este projeto faz analise e visualizacao de dados de corridas (rides) usando um CSV com registros de reservas. Ele le o arquivo `data/ncr_ride_bookings.csv`, limpa alguns campos e gera tres graficos para facilitar o entendimento do comportamento das corridas.

**O que voce vai obter ao executar**
1. Grafico de corridas por hora.
2. Grafico de corridas por dia da semana.
3. Grafico de dispersao entre distancia da corrida e valor da reserva.

---

**Estrutura do projeto**
- `main.py`: ponto de entrada. Carrega o CSV, aplica limpeza e chama os graficos.
- `srs/carregar_dados.py`: funcoes auxiliares para carregar CSVs da pasta `data`.
- `srs/limpeza_dados.py`: regras de limpeza e normalizacao de colunas.
- `srs/visualizacao.py`: funcoes que geram os graficos com matplotlib.
- `data/ncr_ride_bookings.csv`: arquivo de dados principal (baixado do Kaggle).
- `data/Dasboard.gif`: animacao do dashboard (referencia visual).
- `data/Uber.pbix`: arquivo do Power BI (dashboard).

---

**Requisitos**
- Python 3.10+ (recomendado)
- `pandas`
- `matplotlib`
- `openpyxl` (dependencia listada no `requirements.txt`)

---

**Instalacao (passo a passo)**
1. Abra o terminal na pasta do projeto `C:\Users\Matheus\PycharmProjects\PythonProject`.
2. Crie e ative um ambiente virtual:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

3. Instale as dependencias:

```powershell
pip install -r requirements.txt
```

---

**Como obter o CSV do Kaggle**
Voce precisa baixar o arquivo `ncr_ride_bookings.csv` do Kaggle e colocar dentro da pasta `data`.

Forma 1: Download manual
1. Acesse o Kaggle no navegador.
2. Procure pelo dataset relacionado a `ncr_ride_bookings` ou `NCR ride bookings`.
3. Baixe o arquivo `ncr_ride_bookings.csv`.
4. Coloque o arquivo em `data/ncr_ride_bookings.csv`.

Forma 2: Kaggle API (linha de comando)
1. Instale o Kaggle CLI:

```powershell
pip install kaggle
```

2. Configure o arquivo `kaggle.json` com suas credenciais (Kaggle > Settings > API).
3. Baixe o dataset (substitua `<slug-do-dataset>` pelo slug correto do Kaggle):

```powershell
kaggle datasets download -d <slug-do-dataset>
```

4. Extraia o arquivo e mova `ncr_ride_bookings.csv` para `data/`.

---

**Como executar o projeto**
1. Garanta que o arquivo `data/ncr_ride_bookings.csv` existe.
2. Execute o `main.py`:

```powershell
python main.py
```

Ao executar, tres janelas de graficos vao aparecer (uma de cada vez). Feche a janela do grafico para ver o proximo.

---

**Fluxo logico do projeto (explicacao simples)**
1. `main.py` carrega o CSV da pasta `data`.
2. O DataFrame e enviado para `limpeza_dados`.
3. A limpeza combina `Date` e `Time` em `date`, cria `hora` e `dia_semana`, padroniza `Payment Method` e normaliza `Cancelled Rides by Driver`.
4. Os dados limpos sao usados para gerar tres graficos: corridas por hora, corridas por dia da semana e distancia x valor.

---

**Detalhamento dos arquivos**

`main.py`
- Localiza o CSV em `data/ncr_ride_bookings.csv`.
- Le o arquivo com `pandas.read_csv`.
- Aplica `limpeza_dados`.
- Chama tres funcoes de grafico.

`srs/limpeza_dados.py`
- `_coluna_por_nome`: procura colunas ignorando maiusculas/minusculas.
- `_limpar_date`: combina `Date` e `Time`, cria `hora` e `dia_semana`.
- `_limpar_payment_method`: padroniza meios de pagamento.
- `_limpar_cancelled_rides_by_driver`: transforma cancelamentos em 0 ou 1.
- `limpeza_dados`: executa todas as etapas acima.

`srs/visualizacao.py`
- `grafico_corridas_horas`: grafico de barras com contagem por hora.
- `grafico_dia_semana`: grafico de barras com contagem por dia.
- `grafico_distancia_preco`: grafico de dispersao entre distancia e valor.
- Todas as funcoes chamam `limpeza_dados` para garantir consistencia.

`srs/carregar_dados.py`
- `carregar_csvs_da_pasta_data`: le todos os CSVs dentro de `data`.
- `carregar_ncr_ride_bookings`: le apenas `ncr_ride_bookings.csv`.
- Pode ser usado para testes rapidos ou exploracao.

---

**Possiveis problemas e solucoes**
- Erro `FileNotFoundError`: verifique se o CSV esta em `data/ncr_ride_bookings.csv`.
- Erro de colunas ausentes: confira se o CSV tem `Date`, `Time`, `Payment Method`, `Cancelled Rides by Driver`, `Booking Value`, `Ride Distance`.
- Graficos nao aparecem: use um ambiente que suporte GUI e confirme que `matplotlib` esta instalado.

---


