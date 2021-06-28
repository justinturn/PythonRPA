import csv
import os
import os
import glob
import pandas as pd


out_fnam = r'C:\Users\jturner\testProj\FilesToClean\final.csv'
directory = r'C:\Users\jturner\testProj\FilesToClean\Process'

# COMBINE
# with open(out_fnam, 'w', newline='') as out_file:
#     for inputFileToClean in os.listdir(directory):
#         inputFileTotalName = directory + os.sep + inputFileToClean
#         with open(inputFileTotalName) as in_file:
#             writer = csv.writer(out_file)
#             for row in csv.reader(in_file):
#                 if any(field.strip() for field in row):
#                     writer.writerow(row)

df = pd.DataFrame()
df = pd.read_csv(r'C:\Users\jturner\testProj\joined.csv')

df.drop_duplicates(subset='RegNum')

df.to_csv(r'C:\Users\jturner\testProj\FilesToClean\finalCLEANED.csv')
