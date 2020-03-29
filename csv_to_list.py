import csv
import json
from datetime import datetime

data = []

with open('../CPTR 141 (2204).csv') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		print(row['zyBook'], row['Date'])
		if not row['zyBook']:
			continue
		new_row = []
		formatted_zybook = "zyBook " + row['zyBook']
		new_row.append(formatted_zybook)
		formatted_date = datetime.strptime(row['Date'], "%d-%b").strftime("%-m/%-d/2020")
		new_row.append(formatted_date)
		data.append(new_row)

with open('fundamentals', 'w') as writefile:
	json.dump(data, writefile)