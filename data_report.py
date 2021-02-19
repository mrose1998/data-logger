#!/usr/bin/env python3
#Michala Rose
#Made in order to filter .csv files in an easier fashion

import os
import sys
import csv
import time
import PySimpleGUI as sg
from operator import itemgetter 
from datetime import datetime

def process_data(path):
    file = open(path, newline='') #can put any file
    csv_reader = csv.reader(file)
    for i in range(18):
        next(csv_reader)
    header = next(csv_reader)
    #print(header)
    #sets up the 2d array of proper type
    data = []
    for row in csv_reader:
	# row = [P1, P2, Time, Date]
        p1 = float(row[0])
        p2 = row[1]
        time = datetime.strptime(row[2], '%H:%M').strftime('%H:%M')
        date = row[3]
        data.append([p1, p2, time, date])
    sizeData = len(data)
    #print(sizeData)

    #initialize variables and list
    dateCurr = data[0][3]
    #print(dateCurr)
    tempTime = list()
    masterList = list()
    masterList.append(['Date', 'Minimum Temperature', 'Maximum Temperature'])

    for i in range(sizeData):
        if data[i][3] == dateCurr:
            #adds temp and time to the list 
            tempTime.append((data[i][0], data[i][2]))
        else:
            tempTime.sort(key=lambda el:el[0])
            masterList.append([dateCurr, tempTime[0], tempTime[len(tempTime)-1]])
            tempTime.clear()
            dateCurr = data[i][3] #set new date
            tempTime.append((data[i][0], data[i][2]))
    return masterList

def main():
    dataL = process_data("data.csv")
    for x in dataL:
        print(x)

if __name__ == "__main__":
    main()