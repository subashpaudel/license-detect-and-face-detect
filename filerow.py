import csv

column_values = set()
new_rows = []

with open('file.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        if (row[0] in column_values):
            continue
        column_values.add(row[0])
        new_rows.append(row)
        print(new_rows)

##with open('updated.csv', 'w') as csvfile:
##    writer = csv.writer(csvfile)
##    writer.writerows(new_rows)
