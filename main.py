import pandas as pd

# Replace 'your_file.csv' with the path to your CSV file
file_path = 'Statement.csv'

df = pd.read_csv(file_path)

df['S / L'] = pd.to_numeric(df['S / L'], errors='coerce')
df['Price'] = pd.to_numeric(df['Price'], errors='coerce')
df['Size'] = pd.to_numeric(df['Size'], errors='coerce')

total_slippage_loss = 0
slippage_counter = 0

# Loop through each row in the DataFrame
for index, row in df.iterrows():
    if pd.notna(row['S / L']):
        if row['Type'] == 'buy':
            slippage_loss = (row['S / L'] - row['Price']) * row['Size']
        elif row['Type'] == 'sell':
            slippage_loss = (row['Price'] - row['S / L']) * abs(row['Size'])
        else:
            continue  # Skip if the 'Type' is not 'buy' or 'sell'

        if slippage_loss > 0:
            total_slippage_loss += slippage_loss
            slippage_counter += 1

# Print the total slippage loss and the number of occurrences with slippage
print("Total Slippage Loss:", total_slippage_loss)
print("Number of Occurrences with Slippage:", slippage_counter)
