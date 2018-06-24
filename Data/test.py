import os
import time
import sys
import datetime
import json


def it():
    # provide txt file
    slices = [(0, 3), (3, 24), (24, 45), (45, 53), (53, 61), (61, 62), (62, 64), (64, 83), (83, 85), (85, 115), (115, 145), (145, 146)]
    start_time = time.time()
    data_list = [[line[slice(start, end)].strip() for start, end in [part for part in slices]] for line in open(os.getcwd() + '\\B3902V.TXT', 'r')]

    data_list_srt = sorted(data_list, key=lambda x: x[1])

    date = datetime.date.today()
    date_string = date.strftime('%y%m%d')

    with open(date_string + '_' + 'variant_data_raw', 'w') as f:
        json.dump(data_list_srt, f, indent=4, sort_keys=True, ensure_ascii=False)

    # print(sys.getsizeof(txtfile), "--- %s GB's ---" % int(sys.getsizeof(txtfile) / 10000000))
    print("--- %s seconds ---" % (time.time() - start_time))
    print("concluded")


it()
