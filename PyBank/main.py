import os
import csv

#analyze data
file_path = os.path.join('Resources','budget_data.csv')

month_counter = 0
net_profit = 0
profit_change = []
prev_month = 0
greatest_increase = 0
greatest_decrease = 0
high_month = ''
low_month = ''

with open(file_path) as csv_file:
	csvreader = csv.reader(csv_file,delimiter=',')

	header = next(csvreader)
	#print(header)
	start_flag = True
	for month in csvreader:
		dif = int(month[1])-prev_month
		month_counter += 1
		net_profit += int(month[1])

		if start_flag == False:
			profit_change.append(dif)

			if dif > greatest_increase:
				greatest_increase = dif
				high_month = month[0]
			if dif < greatest_decrease:
				greatest_decrease = dif
				low_month = month[0]
		start_flag = False

		prev_month = int(month[1])
avg = round(sum(profit_change)/len(profit_change),2)

#print out results
print('Financial Analysis')
print('---------------------------')
print(f"Total Months: {month_counter}")
print(f"Total: ${net_profit}")
if avg < 0:
	print(f"Average Change: -${0-avg}")
else:
	print(f"Average Change: ${avg}")
print(f"Greatest Increase in Profits: {high_month} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {low_month} (-${0-greatest_decrease})")

output = os.path.join('Analysis','financial_analysis.txt')

#write txt file
write = open(output,'w')
write.write(f"Financial Analysis\n\
---------------------------\n\
Total Months: {month_counter}\n\
Total: ${net_profit}\n\
Average Change: ${avg}\n\
Greatest Increase in Profits: {high_month} (${greatest_increase})\n\
Greatest Decrease in Profits: {low_month} (-${0-greatest_decrease})")