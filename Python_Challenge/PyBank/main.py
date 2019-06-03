import os
import csv

os.chdir(os.path.dirname(__file__))
path = os.path.join("Resources", "budget_data.csv")

with open(path, newline = "") as csv_file:
    csv_object = csv.reader(csv_file, delimiter = ",")

    # skip header
    header = next(csv_object)
    
    months = []
    net_total = 0
    
    first = True

    for row in csv_object: 
        if row[0] not in months:
            months.append(row[0])

        if first: 
            # initiate as the data (month and Profit/Loss) in the first month
            increase_mon = decrease_mon = row[0]
            increase_val = decrease_val = int(row[1])
            prev_val = change = net_change_0 = int(row[1])
            first = False
        else: 
            change = int(row[1]) - prev_val
            prev_val = int(row[1])

            # find greatest increase & decrease changes
            if  change > increase_val: 
                increase_mon = row[0]
                increase_val = change
            if change < decrease_val:
                decrease_mon = row[0]
                decrease_val = change
        
        net_total += int(row[1]) 
    
    # the net change is only related to the first and last Loss/Profit, 
    # so net_change calculation is operated out of the forloop 
    # (for faster operation)
    net_change = int(row[1]) - net_change_0

    # store summary table content in a string
    print_str =  """
    Financial Analysis
    ----------------------------
    Total Months: {}
    Total: ${}
    Average Change: ${:.2f}
    Greatest Increase in Profits: {} (${})
    Greatest Increase in Profits: {} (${})
    """.format(len(months), 
                net_total, 
                net_change/(len(months) -1),
                increase_mon, increase_val,
                decrease_mon, decrease_val)

    # print to screen and .txt
    print(print_str)
    f = open("summary.txt", "w+")
    f.write(print_str)
    f.close()
