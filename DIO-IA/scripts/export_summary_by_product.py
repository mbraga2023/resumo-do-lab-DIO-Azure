import pandas as pd
from pathlib import Path

# Caminhos das pastas
base_dir = Path(__file__).resolve().parent.parent
raw_data_dir = base_dir / "data" / "raw_data"
output_dir = base_dir / "data" / "processed_data"
output_dir.mkdir(parents=True, exist_ok=True)

# Carregar arquivos CSV
aliexpress_df = pd.read_csv(raw_data_dir / "Meganium_Sales_Data_-_AliExpress.csv")
etsy_df = pd.read_csv(raw_data_dir / "Meganium_Sales_Data_-_Etsy.csv")
shopee_df = pd.read_csv(raw_data_dir / "Meganium_Sales_Data_-_Shopee.csv")

# Unir os dados
combined_df = pd.concat([aliexpress_df, etsy_df, shopee_df], ignore_index=True)

# Resumo por produto
sales_by_product = (
    combined_df.groupby("product_sold")
    .agg(total_quantity_sold=("quantity", "sum"),
         total_revenue=("total_price", "sum"),
         average_unit_price=("unit_price", "mean"))
    .reset_index()
    .sort_values(by="total_quantity_sold", ascending=False)
)

# Vendas por produto e país
sales_by_product_country = (
    combined_df.groupby(["product_sold", "delivery_country"])
    .agg(total_quantity_sold=("quantity", "sum"),
         total_revenue=("total_price", "sum"))
    .reset_index()
    .sort_values(by=["product_sold", "total_quantity_sold"], ascending=[True, False])
)

# Vendas por produto e site
sales_by_product_site = (
    combined_df.groupby(["product_sold", "site"])
    .agg(total_quantity_sold=("quantity", "sum"),
         total_revenue=("total_price", "sum"))
    .reset_index()
    .sort_values(by=["product_sold", "total_quantity_sold"], ascending=[True, False])
)

# Exportar para Excel
output_file = output_dir / "vendas_meganium.xlsx"
with pd.ExcelWriter(output_file, engine="xlsxwriter") as writer:
    sales_by_product.to_excel(writer, sheet_name="Resumo por Produto", index=False)
    sales_by_product_country.to_excel(writer, sheet_name="Por País", index=False)
    sales_by_product_site.to_excel(writer, sheet_name="Por Plataforma", index=False)

print(f"✅ Planilha criada com sucesso: {output_file}")
