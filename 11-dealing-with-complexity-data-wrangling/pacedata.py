row_data = {}

with open('pacedata.csv') as paces:
    column_headings = paces.readline().strip().split(',')
    column_headings.pop(0)

    for each_line in paces:
        row = each_line.strip().split(',')
        row_label = row.pop(0)
        inner_dict = {}
        for i in range(len(column_headings)):
            inner_dict[row[i]] = column_headings[i]
        row_data[row_label] = inner_dict

# page 408
# column_heading = row_data['15k']['43:24']

# prediction = [
#     k for k in row_data['20k'].keys() if row_data['20k'][k] == column_heading
# ]

# print(prediction)
