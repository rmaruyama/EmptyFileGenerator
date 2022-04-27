# Empty File Generator
#
# How to use:
#   1. Change "init.txt"
#   2. Change NUMBER_OF_TIMES, which is the number of files you generate
#   3. Run
#
# Input
#   "init.txt" format:
#       line1: YYYYMMDD  # date
#       line2: N         # number
#   - "init.txt" will be updated after run the program to prepare the next run.
# OUTPUT
#   file name format:
#       (YYYYMMDD)_(NNNN).txt
#       example: 20220401_0001.txt
#   - Both date & number increase by 1 each time a file is generated.

import datetime

NUMBER_OF_TIMES = 7  # the number of files you generate

if __name__ == '__main__':
    with open("init.txt", mode='r') as f:
        date_str = f.readline()[0:8]  # cancel "\n"
        sequence_str = f.readline()

    for _ in range(NUMBER_OF_TIMES):
        # make a file name
        file_name = date_str + "_" + sequence_str.zfill(4) + ".txt"
        # make a file
        with open(file_name, mode='w') as f:
            pass

        # increment date
        d = datetime.date(int(date_str[0:4]), int(date_str[4:6]), int(date_str[6:8]))
        d = d + datetime.timedelta(days=1)
        date_str = d.strftime("%Y%m%d")
        # increment sequence
        sequence = int(sequence_str)
        sequence += 1
        sequence_str = str(sequence)

    # update init.txt
    with open("init.txt", mode='w') as f:
        f.write(date_str + "\n")
        f.write(sequence_str)
