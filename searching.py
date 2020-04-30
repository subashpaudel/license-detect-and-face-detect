import csv
platenumber =input('Enter plate number to find\n')

first_time_line = None

with open('file.csv', 'r') as csvfile:
    datareader = csv.reader(csvfile)
    for line, row in enumerate(datareader):
        try:
            first_column = row[0]
        except IndexError:
            continue
        else:
            # the file oddly saves with a space after TIME
            if first_column.strip() == platenumber: 
                print(row)
                if first_time_line is None:
                    first_time_line = line
