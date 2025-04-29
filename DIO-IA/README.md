# 📊 Análise de Vendas - Meganium

Este projeto realiza uma análise completa das vendas dos produtos **Meganium** em três plataformas de e-commerce: **AliExpress**, **Etsy** e **Shopee**. Os dados são processados com **Python** e exportados em formato Excel para geração de relatórios.

---

## 🗂️ Base de Dados

- Fonte: 3 arquivos CSV (um por plataforma).
- Informações: produto vendido, quantidade, preço, moeda, cupom, país de entrega, dados do comprador e faturamento.

---

## 🎯 Prompts Respondidos com Python

### 1. **Resumo Geral por Produto**
**Script:** `export_summary_by_product.py`  
> Total de unidades vendidas, receita e preço médio por produto. Inclui também análises por país e plataforma.

### 2. **Tendência Mensal de Vendas (USD)**
**Script:** `export_monthly_trend_usd.py`  
> Exibe a evolução mensal das vendas por plataforma, com receita convertida para dólares (USD).

### 3. **Produtos Mais Lucrativos por Plataforma**
**Script:** `export_revenue_by_platform.py`  
> Indica quais produtos geram mais receita em cada plataforma, com preços normalizados em USD.

### 4. **Uso de Cupons por País**
**Script:** `export_discounts_by_country.py`  
> Mostra onde os cupons são mais utilizados e onde há maior volume de descontos concedidos.

---

## 🛠️ Tecnologias Utilizadas

- Python 3.13+
- pandas
- xlsxwriter
- pathlib

---

## ▶️ Como Executar

1. Instale as dependências (em um ambiente virtual, se preferir):
   ```bash
   pip install pandas xlsxwriter

2. Execute qualquer script desejado:
   ```bash
python scripts/export_summary_by_product.py

3. Os arquivos Excel gerados ficarão disponíveis na pasta:
   ```bash
data/processed_data/

---

## 💡 Observações

- Todos os valores monetários são convertidos para **USD**, utilizando taxas de câmbio fixas.
- Os nomes das abas do Excel evitam caracteres inválidos para compatibilidade com o formato.
- Os scripts utilizam a biblioteca `xlsxwriter` para melhor formatação dos arquivos Excel.

---

## 👤 Autor

Projeto desenvolvido como parte do curso **DIO - Inteligência Artificial aplicada aos negócios**.  

📎 **Projeto original (projeto base)** disponível em:  
https://github.com/digitalinnovationone/dataset-gamesshop/