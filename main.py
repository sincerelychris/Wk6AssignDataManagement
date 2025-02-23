import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

file_path = 'sampledatafoodsales(FoodSales).csv'
df = pd.read_csv(file_path)
print("First 5 & Last 5:")
print(df)
print("\nHead of the file:")
print(df.head())

print("\nDescription of the file:")
print(df.describe())

print("\nProduct names and unit prices:")
for product, price in zip(df['Product'], df['UnitPrice']):
    print(f"{product}, {price}")

#products_and_prices = df[['Product', 'UnitPrice']]
#print(products_and_prices.to_string(index=False))



# Ploting evrythinh
plt.figure(figsize=(10, 5))
plt.bar(df['Product'], df['UnitPrice'])
plt.xlabel('Product')
plt.ylabel('UnitPrice')
plt.title('Product Name vs. unit Price')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()
