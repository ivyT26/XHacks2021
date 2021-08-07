"""
This python script analyzes two datasets and quickly allows administrators
to view the attendance as well as duration of the participants.
"""

#Importing pandas library
import pandas as pd

#Importing datasets
attendance_dataset = pd.read_csv('Zoom Attendance.csv')

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

#Importing class list
class_list = pd.read_csv('Class List.csv') #Make sure it is a 1 column dataset with header (Ex: "Students")

#Adding "Present" and "Duration" columns to dataset, and setting all values to 0
class_list["Present"] = [0 for i in range(len(class_list))]
class_list["Duration"] = [0 for i in range(len(class_list))]
class_list.columns = ["Student", "Present", "Duration (Min)"]

#Iterating through attendance data to check if all students were there
for i in range(len(class_list)):
  if class_list.loc[i][0] in [i for i in attendance_revised.iloc[:,0]]:
    class_list["Present"][i] = 1
    class_list["Duration (Min)"][i] = [i for i in attendance_revised.iloc[:,1]][[x for x in attendance_revised.iloc[:,0]].index(class_list.loc[i][0])]
  else:
    class_list["Present"][i] = 0

#Sorting dataframe based on duration length
class_list = class_list.sort_values(by=["Duration (Min)"])

#View results
print(class_list)
