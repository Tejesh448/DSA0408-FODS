import pandas as pd

data = {
    'Product': ['Laptop', 'Mobile', 'Laptop', 'Headphones',
                'Mobile', 'Tablet', 'Laptop', 'Headphones'],
    'Quantity': [10, 20, 15, 25, 30, 12, 20, 15]
}

df = pd.DataFrame(data)

sales = df.groupby('Product')['Quantity'].sum()

top_products = sales.sort_values(ascending=False).head(5)

print("Top 5 Best-Selling Products:")
print(top_products)
