import os
import time
import sys
import datetime
import json


def it():
    # provide txt file
    # (62, 64), (64, 83), (83, 85), (115, 145)
    slices = [(0, 3), (3, 24), (24, 45), (45, 53), (53, 61), (61, 62), (85, 115), (145, 146)]
    start_time = time.time()
    data_list = set(tuple(line[slice(start, end)].strip()
                          for start, end in [part for part in slices])
                    for line in open(os.getcwd() + '\\B3902V - Copia.TXT', 'r'))
    # data_list = set (tuple (line[slice (start, end)].strip () for start, end in [part for part in slices]) for line in
                     # open (os.getcwd () + '\\B3902V.TXT', 'r'))

    data_list_to_srt = list(data_list)
    print(sys.getsizeof(data_list), sys.getsizeof(data_list_to_srt))
    data_list_srt = sorted(data_list_to_srt, key=lambda x: x[1])

    date = datetime.date.today()
    date_string = date.strftime('%y%m%d')

    with open(date_string + '_' + 'variant_data_raw.json', 'w') as f:
        json.dump(data_list_srt, f, indent=4, sort_keys=True, ensure_ascii=False)

    # print(sys.getsizeof(txtfile), "--- %s GB's ---" % int(sys.getsizeof(txtfile) / 10000000))
    print("--- %s seconds ---" % (time.time() - start_time))
    print("concluded")


def it2():
    # provide txt file
    # (62, 64), (64, 83), (83, 85), (115, 145)
    # (0, 3)
    slices = [(3, 24), (62, 64), (64, 83), (83, 85), (115, 145), (85, 115)]
    start_time = time.time()
    data_list = [[line[slice(start, end)].strip()
                 for start, end in [part for part in slices]]
                 for line in open(os.getcwd() + '\\B3902V - Copia.TXT', 'r')]

    """
     data_list = set (tuple (line[slice (start, end)].strip () for start, end in [part for part in slices])
     for line in open (os.getcwd () + '\\B3902V.TXT', 'r'))
    """

    data_list_srt = sorted(data_list, key=lambda x: x[0])

    for index, obj in enumerate(data_list_srt):
        if index == 0:


    date = datetime.date.today()
    date_string = date.strftime('%y%m%d')

    with open(date_string + '_' + 'variant_data_raw.json', 'w') as f:
        json.dump(data_list_srt, f, indent=4, sort_keys=True, ensure_ascii=False)

    # print(sys.getsizeof(txtfile), "--- %s GB's ---" % int(sys.getsizeof(txtfile) / 10000000))
    print("--- %s seconds ---" % (time.time() - start_time))
    print("concluded")


it()
