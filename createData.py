import csv
from main import *

csv_file_path = 'dataset.csv'

scraped_data = getPunk()

with open(csv_file_path, mode='a', newline='', encoding='utf-8') as file:
    fieldnames = ["content", "value"]
    writer = csv.writer(file)
    for data in scraped_data:
        writer.writerow([data, 0])

print(f"Scraped data has been saved to {csv_file_path}")