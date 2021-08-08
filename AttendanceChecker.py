"""
This python script analyzes two datasets and quickly allows administrators
to view the attendance as well as duration of the participants.
"""

#Importing pandas library
import pandas as pd

#Importing system libraries
import os
import sys
import warnings

#Checking length of input arguments
if len(sys.argv) != 3:
    sys.exit("\nUsage: python Attendance_Checker.py Zoom-Attendance-CSV-Directory Class-List-CSV-Directory.csv\n")

#Importing Zoom attendance dataset
attendance_dataset = pd.read_csv(sys.argv[1])

#Removing incorrect attendance header
attendance_dataset.columns = ["" for col in attendance_dataset]

#Removing row 0 as it is incorrect
attendance_dataset = attendance_dataset.drop([0])

#Getting new headers
new_headers = attendance_dataset.iloc[0].item().split(",")

#Creating new dataset
attendance_revised = pd.DataFrame(columns = new_headers)

#Iterating through values and adding them to new dataset
for i in range(1, len(attendance_dataset)):
  attendance_revised.loc[i] = attendance_dataset.iloc[i].item().split(",")

#Removing Email and Guest columns
del attendance_revised["User Email"]
del attendance_revised["Guest"]

#Renaming columns
attendance_revised.columns = ["Name", "Duration (Min)"]

#Importing class list dataset
class_list = pd.read_csv(sys.argv[2])

#Adding "Present" and "Duration" columns to dataset, and setting all values to 0
class_list["Present"] = [0 for i in range(len(class_list))]
class_list["Duration"] = [0 for i in range(len(class_list))]
class_list.columns = ["Student", "Present", "Duration (Min)"]

#Hiding warning
warnings.filterwarnings("ignore")

#Iterating through attendance data to check if all students were there
for i in range(len(class_list)):
  if class_list.loc[i][0] in [i for i in attendance_revised.iloc[:,0]]:
    class_list["Present"][i] = 1
    class_list["Duration (Min)"][i] = [i for i in attendance_revised.iloc[:,1]][[x for x in attendance_revised.iloc[:,0]].index(class_list.loc[i][0])]
  else:
    class_list["Present"][i] = 0

#Sorting dataframe based on duration
class_list = class_list.sort_values(by=["Duration (Min)"])

#View results
print("\n\t\t\t\t\tAttendance Comparison Results")
print("The following students were absent:")

missing_count = 0
for i in range(len(class_list)):
  if class_list.loc[i][1] == 0:
    missing_count += 1
    print(f"{missing_count}. {class_list.loc[i][0]}")

#Check if no students were missing
if missing_count == 0:
  print("N/A - Full Attendance!")

print("\n\tOverall Summary:")
print(class_list.to_string(index=False))
print("\n")
