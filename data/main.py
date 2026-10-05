# Dateien lesen und schreiben mit CSV & JSON 

import csv
from pathlib import Path 
from person import Person

people = []

data_dir = Path("./data")
csv_file = data_dir / "people.csv"

print("Start reading CSV file...")
with csv_file.open("r", newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile) 
    for row in reader:
        new_person = Person.from_dict(row)
        people.append(new_person)
print("Stopped reading CSV file.")


print(people)



output_dir = Path("./output")
output_dir.mkdir(exist_ok=True)
csv_output_file = output_dir / "new_data.csv" 


print("Write CSV file...")
with csv_output_file.open("a", newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames= Person.fieldnames())
    writer.writeheader()
    writer.writerows([p.to_dict()for p in people])
print("Stopped writing CSV file.") 