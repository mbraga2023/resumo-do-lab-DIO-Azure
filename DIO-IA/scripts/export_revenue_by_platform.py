import pandas as pd
from pathlib import Path

# Diretórios
base_dir = Path(__file__).resolve().parent.parent
raw_data_dir = base_dir / "data" / "raw_data"
output_dir = base_dir / "data" / "processed_data"
output_dir.mkdir(parents=True, exist_ok=True)

# Carregar arquivos CSV
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

# Combinar todos os dados
combined_df = pd.concat([aliexpress_df, etsy_df, shopee_df], ignore_index=True)

# Taxas de câmbio para USD
currency_rates = {
    "USD": 1.00,
    "EUR": 1.07,
    "GBP": 1.25
}

# Converter preços para USD
combined_df["currency"] = combined_df["currency"].str.upper()
combined_df["unit_price_usd"] = combined_df.apply(
    lambda row: row["unit_price"] * currency_rates.get(row["currency"], 1.0), axis=1
)
combined_df["total_price_usd"] = combined_df.apply(
    lambda row: row["total_price"] * currency_rates.get(row["currency"], 1.0), axis=1
)

# Agrupar por produto e site
profit_by_product_site = (
    combined_df.groupby(["product_sold", "site"])
    .agg(
        total_quantity_sold=("quantity", "sum"),
        total_revenue_usd=("total_price_usd", "sum"),
        average_unit_price_usd=("unit_price_usd", "mean")
    )
    .reset_index()
    .sort_values(by="total_revenue_usd", ascending=False)
)

# Exportar para Excel com nome de aba válido
output_file = output_dir / "lucro_produto_por_site.xlsx"
with pd.ExcelWriter(output_file, engine="xlsxwriter") as writer:
    profit_by_product_site.to_excel(writer, sheet_name="Lucro por Produto - Site", index=False)

print(f"💹 Arquivo criado com sucesso: {output_file}")
