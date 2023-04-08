#!/usr/bin/env python3

import datetime,time 

file_name='out_file_%s.txt'%str(datetime.datetime.now().strftime("%m_%d_%Y_%H_%M_%S"))
print(file_name)

with open(file_name, "w") as file:
    file.write("Looks that the script is executed")

import os 

os.system('gsutil cp %s gs://ocdebase/'%file_name)

time.sleep(10)

os.system('gcloud compute instances delete scheduled-instance --project project-nnog-hariskhan --zone us-central1-a --quiet')
