import os
import csv

os.chdir(os.path.dirname(__file__))

path = os.path.join("Resources", "election_data.csv")

with open(path, newline = "") as csv_object:
    header = next(csv_object).rstrip("\r\n").split(",")
    rows = csv.reader(csv_object, delimiter = ",")
    
    vote_cnt = {}
    total_cnt = 0

    # store result in dictionay
    for row in rows:
        if row[2] not in vote_cnt:
            vote_cnt[row[2]] = 1
        else:
            vote_cnt[row[2]] = vote_cnt.get(row[2]) + 1

        total_cnt += 1
    
    # create header for the summary table
    print_str = """
Election Results
-------------------------
Total Votes: {}
-------------------------
""".format(total_cnt)

    first = True
    for candidate in vote_cnt:
        vote = vote_cnt.get(candidate)

        #concatinate voting result
        print_str += "{}: {:.3f}% ({})\n".format(candidate, vote/ total_cnt*100, vote)

        # find winner
        if first:
            winner = candidate
            first = False
        else:
            if vote > vote_cnt.get(winner):
                winner = candidate

    # print winner result
    print_str += "-------------------------\nWinner: {}\n-------------------------\n".format(winner)
    
    # print to screen and .txt
    print(print_str)
    f=open("summary.txt", "w+")
    f.write(print_str)
    f.close()