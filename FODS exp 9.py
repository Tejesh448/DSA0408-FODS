import pandas as pd

data = {
    'Property_ID': [101, 102, 103, 104, 105],
    'Location': ['Chennai', 'Madurai', 'Chennai', 'Coimbatore', 'Madurai'],
    'Bedrooms': [3, 5, 4, 6, 2],
    'Area': [1200, 1800, 1500, 2200, 1000],
    'Price': [5000000, 7500000, 6000000, 9000000, 4000000]
}

property_data = pd.DataFrame(data)

print("Average Listing Price by Location:")
print(property_data.groupby('Location')['Price'].mean())

count = property_data[property_data['Bedrooms'] > 4].shape[0]
print("\nProperties with more than 4 bedrooms:", count)

largest = property_data.loc[property_data['Area'].idxmax()]
print("\nProperty with Largest Area:")
print(largest)
