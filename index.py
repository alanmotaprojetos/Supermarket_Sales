import pandas as pd

df_data = pd.read_csv("supermarket_sales.csv")
df_data

# 1 - Faturamento total por filial:
faturamento = df_data.groupby("City")["Total"].sum()
print(faturamento)

# 2 - Renda bruta por filial
renda_bruta = df_data.groupby("City")["gross income"].sum()
print(renda_bruta)

# 3 - Métodos de Pagamento - Payment 
payment = df_data.groupby("Payment")["Total"].sum()
print(payment)

# 4 - Segmentação das Vendas - (Product line and Quantity)
percentual = df_data.groupby("Product line")["Total"].sum()/df_data.groupby("Product line")["Total"].sum().sum()*100
print(percentual)

# 5 - Percentual de participação de cada tipo de produto:

percentual = df_data.groupby("Product line")["Total"].sum()/df_data.groupby("Product line")["Total"].sum().sum()*100
print("Percentual total: {}".format(percentual))

# 6 - Consumo distribuído por Gênero
df_data.groupby(["Product line", "Gender",])[["Total"]].sum().pivot_table(index="Product line", columns="Gender")


# 7 - Faturamento por Mês

df_data["Date"] = pd.to_datetime(df_data["Date"])
df_data["Month"] = df_data["Date"].apply(lambda x: x.month)
df_data["Year"] = df_data["Date"].apply(lambda x: x.year)
df_data.groupby(["Month"])["Total"].sum()
df_data.groupby(["Year"])["Total"].sum()

# 8 - Média de avaliação por cada filial de 2019?
df_data.groupby("City")["Rating"].mean()

# 9 - Média de avaliação por cada filial em Janeiro de 2019?
df_data[(df_data["Year"] == 2019) & (df_data["Month"] == 1)]["Rating"].mean()

# 10 - Distribuição dos gastos pro tipo de consumidor em cada filial:
df_data.groupby(["Customer type", "City"])["Total"].sum()

