import pandas as pd
from pathlib import Path

# Diretórios
base_dir = Path(__file__).resolve().parent.parent
raw_data_dir = base_dir / "data" / "raw_data"
output_dir = base_dir / "data" / "processed_data"
output_dir.mkdir(parents=True, exist_ok=True)

# Carregar dados
aliexpress_df = pd.read_csv(raw_data_dir / "Meganium_Sales_Data_-_AliExpress.csv")
etsy_df = pd.read_csv(raw_data_dir / "Meganium_Sales_Data_-_Etsy.csv")
shopee_df = pd.read_csv(raw_data_dir / "Meganium_Sales_Data_-_Shopee.csv")

# Normalizar colunas
for df in [aliexpress_df, etsy_df, shopee_df]:
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

# Adicionar 'site'
aliexpress_df["site"] = "AliExpress"
etsy_df["site"] = "Etsy"
shopee_df["site"] = "Shopee"

# Combinar dados
combined_df = pd.concat([aliexpress_df, etsy_df, shopee_df], ignore_index=True)

# Normalizar moeda
currency_rates = {
    "USD": 1.00,
    "EUR": 1.07,
    "GBP": 1.25
}
combined_df["currency"] = combined_df["currency"].str.upper()
combined_df["discount_value_usd"] = combined_df.apply(
    lambda row: row["discount_value"] * currency_rates.get(row["currency"], 1.0), axis=1
)

# Filtrar pedidos com cupom
discounted_orders = combined_df[combined_df["discount_coupon"].notnull()]

# Agrupar por país
discounts_by_country = (
    discounted_orders.groupby("delivery_country")
    .agg(
        orders_with_coupon=("discount_coupon", "count"),
        total_discount_value=("discount_value_usd", "sum"),
        average_discount_per_order=("discount_value_usd", "mean")
    )
    .reset_index()
    .sort_values(by="total_discount_value", ascending=False)
)

# Exportar para Excel
output_file = output_dir / "descontos_por_pais.xlsx"
with pd.ExcelWriter(output_file, engine="xlsxwriter") as writer:
    discounts_by_country.to_excel(writer, sheet_name="Descontos por País", index=False)

print(f"🔖 Relatório de descontos exportado: {output_file}")
