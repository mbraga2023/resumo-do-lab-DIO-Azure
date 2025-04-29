import pandas as pd
from pathlib import Path

# Diretórios
base_dir = Path(__file__).resolve().parent.parent
raw_data_dir = base_dir / "data" / "raw_data"
output_dir = base_dir / "data" / "processed_data"
output_dir.mkdir(parents=True, exist_ok=True)

# Carregar arquivos
aliexpress_df = pd.read_csv(raw_data_dir / "Meganium_Sales_Data_-_AliExpress.csv")
etsy_df = pd.read_csv(raw_data_dir / "Meganium_Sales_Data_-_Etsy.csv")
shopee_df = pd.read_csv(raw_data_dir / "Meganium_Sales_Data_-_Shopee.csv")

# Normalizar nomes das colunas
for df in [aliexpress_df, etsy_df, shopee_df]:
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

# Adicionar coluna 'site'
aliexpress_df["site"] = "AliExpress"
etsy_df["site"] = "Etsy"
shopee_df["site"] = "Shopee"

# Combinar os dados
combined_df = pd.concat([aliexpress_df, etsy_df, shopee_df], ignore_index=True)

# Conversão de moeda para USD
currency_rates = {
    "USD": 1.00,
    "EUR": 1.07,
    "GBP": 1.25
}

# Aplicar conversão
combined_df["currency"] = combined_df["currency"].str.upper()
combined_df["total_price_usd"] = combined_df.apply(
    lambda row: row["total_price"] * currency_rates.get(row["currency"], 1.0), axis=1
)

# Converter data
combined_df["date"] = pd.to_datetime(combined_df["date"])
combined_df["month"] = combined_df["date"].dt.to_period("M")

# Agregação por mês e site
monthly_sales = (
    combined_df.groupby(["month", "site"])
    .agg(total_quantity_sold=("quantity", "sum"),
         total_revenue_usd=("total_price_usd", "sum"))
    .reset_index()
    .sort_values(by=["month", "site"])
)

# Exportar para Excel
output_file = output_dir / "tendencia_mensal_vendas_usd.xlsx"
with pd.ExcelWriter(output_file, engine="xlsxwriter") as writer:
    monthly_sales.to_excel(writer, sheet_name="Tendência Mensal USD", index=False)

print(f"💲 Arquivo com receita em USD criado: {output_file}")
