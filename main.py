import json
import pandas as pd

# Load data from a JSON file
with open('SAW.json', 'r', encoding='utf-8') as file:
    airports = json.load(file)

# SAW airport details
column_a = "SAW (Turkey)"

# Prepare lists to hold the data
column_a_list = []
column_b_list = []

# Iterate over each airport and extract the required information
for airport in airports:
    city = airport.get('city', '').title()
    country = airport.get('country', '').title()
    
    # Skip the entry if the country is Turkey
    if country.lower() == 'turkey':
        continue  # Skip this iteration and move to the next

    column_b = f"{city} ({country})"
    column_a_list.append(column_a)
    column_b_list.append(column_b)

# Create a DataFrame
df = pd.DataFrame({
    'Column A': column_a_list,
    'Column B': column_b_list
})

# Write the DataFrame to an Excel file
df.to_excel('output.xlsx', index=False)

