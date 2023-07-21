import os
import csv

csvpath= os.path.join('Resources','budget_data.csv')

total_months= 0
total_net= 0
previous_profitloss= 0
current_profitloss= 0
net_change= 0
net_change_list= []
greatest_increase= 0
greatest_increase_date= ""
greatest_decrease= 0
greatest_decrease_date= ""




with open(csvpath) as csvfile:
    csvreader= csv.reader(csvfile,delimiter=',')
    print(csvreader)

    csv_header= next(csvreader)
    print(f'CSV Header:{csv_header}')
    first_row= next(csvreader)
    previous_profitloss= int(first_row[1])
    total_months=1
    total_net= previous_profitloss

    for row in csvreader:
        current_profitloss= int(row[1])
        total_net=total_net + current_profitloss
        total_months= total_months+1
        net_change= current_profitloss - previous_profitloss
        net_change_list.append(net_change)
        previous_profitloss=current_profitloss

        if(net_change>greatest_increase):
            greatest_increase= net_change
            greatest_increase_date=row[0]
        if (net_change<greatest_decrease):
            greatest_decrease= net_change
            greatest_decrease_date= row[0]

    average_change= sum(net_change_list)/len(net_change_list) 
    print("Financial Analysis")
    print("--------------------")
    print(f'Total Months: {total_months}')
    print(f'Total: ${total_net}')   
    print(f'Average Change: ${average_change}')
    print(f'Greatest Increase in Profits: {greatest_increase_date} ${greatest_increase}')
    print(f'Greatest Decrease in Profits: {greatest_decrease_date} ${greatest_decrease}')

txtfilepath= os.path.join('analysis','budgetanalysis.txt')
with open(txtfilepath,'w') as txtfile:
    txtfile.write(f'Financial Analysis\n')
    txtfile.write(f'--------------------\n')
    txtfile.write(f'Total Months: {total_months}\n')
    txtfile.write(f'Total: ${total_net}\n')
    txtfile.write(f'Average Change: ${average_change}\n')
    txtfile.write(f'Greatest Increase in Profits:{greatest_increase_date} ${greatest_increase}\n')
    txtfile.write(f'Greatest Decrease in Profits:{greatest_decrease_date} ${greatest_decrease}\n')



    