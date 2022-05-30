#!/usr/local/bin/python3

import glob

final_set_of_ips=set()

for file in glob.glob('C:\\Users\\mn.danilin\\Downloads\\config_files\\*.txt'):
#    file_name=str(file)
#    print(file_name)
    f=open(file)
    for str in f:
#        print(str.find("ip address "))
         if str.find("ip address ") > 0:
                str=str.replace("ip address ", "").strip()
                final_set_of_ips.add(str)

for i in final_set_of_ips:
    print(i)








