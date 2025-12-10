import csv
import glob
import os

input_folder = 'data'
output_file = 'data/aggregated_data.csv'

output_rows = []

for file_path in glob.glob(os.path.join(input_folder, '*.csv')):
    with open(file_path, 'r') as csv_file:
        reader = csv.DictReader(csv_file)

        for row in reader:
            if row['product'].strip().lower() == 'pink morsel':
                quantity = float(row['quantity'])
                price = float(row['price'].replace('$', '').strip())
                sales = quantity * price

                output_rows.append({
                    "Sales": round(sales, 2),   
                    "Date": row['date'],
                    "Region": row['region'],
                })

with open(output_file, 'w', newline='') as out_csv_file:
    fieldnames = ["Sales", "Date", "Region"]
    writer = csv.DictWriter(out_csv_file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(output_rows)

print(f"Aggregated data written to {output_file}")