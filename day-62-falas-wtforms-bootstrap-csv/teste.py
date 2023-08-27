import csv

with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
    csv_data = csv.reader(csv_file, delimiter=',')
    list_of_rows = []
    for row in csv_data:
        list_of_rows.append(row)

print(list_of_rows)

# for index, list in enumerate(list_of_rows):
#     print('natalia')

for index, list in enumerate(list_of_rows):
    print('natalia')
    for i in list:
       if index > 0:
           print(i)

