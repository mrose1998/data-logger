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
from tkinter import *
from tkinter import messagebox

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
    # no longer needed masterList.append(['Date', 'Minimum Temperature', 'Maximum Temperature'])

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
            
    for x in masterList:
        print(x)
    return masterList

def write_newFile(list):
    with open('results.csv', 'w', newline="") as resultFile:
        writer = csv.writer(resultFile)
        writer.writerow(['Date', 'Minimum Temperature', 'Time of Min', 'Maximum Tempature', 'Time of Max'])
        for x in list:
             writer.writerow([x[0], (x[1])[0], (x[1])[1], (x[2])[0], (x[2])[1]])

root = Tk()

myLabelS = Label(root, text="Please enter the name of a csv file. \n Be sure to include .csv")
myLabelS.pack()

myEntry = Entry(root, width = 50, borderwidth = 10)
myEntry.pack()
myEntry.insert(0, "Enter file name here")

def runReport():
    filePath = myEntry.get()
    fromBox = "The file name upon click is read as: " + filePath
    myLabel = Label(root, text=fromBox)
    myLabel.pack()
    write_newFile(process_data(filePath))
    
    # call a method that creates a new csv file

button_report = Button(root, text="Get Data", padx = 20, pady = 10, fg = "white", bg = "green", command = runReport)
button_report.pack()

button_exit = Button(root, text ="Quit Program",  padx = 20, pady = 10, fg = "white", bg = "red", command = root.quit)
button_exit.pack()

root.mainloop()

