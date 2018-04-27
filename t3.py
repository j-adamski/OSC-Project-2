#!/usr/bin/env python
import argparse
import time
import datetime
import os
import json

"""time tracker and to do list, T3. Todo list where you can add your tasks, keep track of how long you have been working on them, and save your output to a text file for additional scripting"""
"""T3 is to assist those who struggle with time management through a simple, easy to use to do list time tracker """

def t3Complete(projectName):
    #t3 --complete 'activity'
    inputFile = 'tasks/tasks.json'
    jsonData=open(inputFile).read()
    data = json.loads(jsonData) 

    for k in data:
        if projectName == k['projectName']:
            k['completed'] = True

    with open('tasks/tasks.json', 'w') as f:
        json.dump(data, f)


def t3Report(userChoice):
    #t3 --report active/completed/all
    #active prints out current projects
    #completed prints out only completed projects
    #all prints out the entire json file

    inputFile = 'tasks/tasks.json'
    jsonData=open(inputFile).read()
    jsonToPython = json.loads(jsonData)

    
    if userChoice == 'active':
        for k in jsonToPython:
            if k['completed'] == False:
                print("Projects: ",k['projectName'])
                print("Time Spent: ",  time.strftime("%H:%M:%S", time.gmtime(k['timeSpent'])))
    elif userChoice == 'completed':
        for k in jsonToPython:
            if k['completed'] == True:
                print("Projects: ",k['projectName'])
                print("Time Spent: ", time.strftime("%H:%M:%S", time.gmtime(k['timeSpent'])))
    elif userChoice == 'all':
        for k in jsonToPython:
            print("Projects: ",k['projectName'])
            print("Time Spent: ", time.strftime("%H:%M:%S", time.gmtime(k['timeSpent'])))
            print("Completed (T/F): ",k['completed'])
    else:
        print("Invalid Option. Choose active/completed/all")

def t3Add(projectName):
    #t3 --add 'activity'
    #Adds a new project
    #new entry structure
    add_dict = {"projectName": projectName,"timeSpent":0,"timeStamp":'',"completed":False}


    with open('tasks/tasks.json') as f:
        data = json.load(f)

    data.append(add_dict)

    with open('tasks/tasks.json', 'w') as f:
        json.dump(data, f)

def t3Delete(projectName):
    #t3 --delete 'activity'
    #removes activity when finished
    inputFile = 'tasks/tasks.json'
    jsonData=open(inputFile).read()
    data = json.loads(jsonData) 
    list1=[]
    for k in data:
        #print(type(k))
        if k['projectName'] == projectName:
            print("Found Project. Deleting.")
        else:
            list1.append(k)
    #print(list1)

    with open('tasks/tasks.json', 'w') as file:
                file.write(json.dumps(list1))


def t3Edit(projectName):
    #t3 --edit 'projectName'
    #needs to be able to check that user input the correct format
    inputFile = 'tasks/tasks.json'
    jsonData=open(inputFile).read()
    data = json.loads(jsonData) 

    for k in data:
        if projectName == k['projectName']:
            print("Current Time Is: " + str(k['timeSpent']))    
            newTime = input("Enter New Time In Minutes: ")
            #Converts user input of minutes to seconds
            k['timeSpent'] = float(newTime)

    with open('tasks/tasks.json', 'w') as f:
        json.dump(data, f)

def t3Start(projectName):
    #t3 --start 'projectName'
    inputFile = 'tasks/tasks.json'
    jsonData=open(inputFile).read()
    data = json.loads(jsonData)

    for k in data:
        if projectName == k['projectName']:
            print("Project Time Has Started")
            #currentTime = datetime.datetime.now().strftime('%H%M')
            k['timeStamp'] = time.time()
    with open('tasks/tasks.json', 'w') as f:
        json.dump(data, f)

def t3Stop(projectName):
    #t3 -- stop 'projectName'
    inputFile = 'tasks/tasks.json'
    jsonData=open(inputFile).read()
    data = json.loads(jsonData)

    for k in data:
        if projectName == k['projectName']:
            #check to make sure there is a timestamp
            if k['timeStamp'] == '':
                print("Project has no start time, is not being tracked")
                break
            print("Project Time Has Stopped, Tracked Time Updated")
            elapsedTime = time.time() - k['timeStamp']
            #add new time to current overall project time
            currentProjectTime = k['timeSpent']
            overallProjectTime = currentProjectTime + elapsedTime
            k['timeSpent'] = overallProjectTime
            k['timeStamp'] = ''
            print("Total Project Worktime: " + time.strftime("%H:%M:%S", time.gmtime(overallProjectTime)))
    with open('tasks/tasks.json', 'w') as f:
        json.dump(data, f)



def _main():

    """Run the CLI Interface for T3"""
    #parser
    parser = argparse.ArgumentParser()
    
    parser.add_argument('userParserInput', help="the user input, will be printed if there are no arguments")
    
    parser.add_argument("--add",help="Adds a Project to your list",action='store_true', default=False, dest='addValue')
    parser.add_argument("--complete",help="Marks project on list as completed",action="store_true",default=False,dest="completeValue")
    parser.add_argument("--delete", help="Removes Project from list",action='store_true',default=False,dest='deleteValue')
    parser.add_argument("--report", help="Prints out basic report. Options: active/all/completed  (default=active)",action='store_true', default=False, dest='reportValue',)
    parser.add_argument("--start", help="Starts timing of Project, will overwrite existing tracked time if project is already being tracked",action='store_true',default=False,dest='startValue')
    parser.add_argument("--stop/finish", help="Stops timing of Project, updates total run time", action='store_true',default=False,dest="stopValue")
    parser.add_argument("--edit", help="Edits the time spent on a Project (in minutes)", action='store_true',default=False,dest="editValue")
    results = parser.parse_args()


    if (results.reportValue) == True:
        t3Report(results.userParserInput)
    if (results.addValue) == True:
        #t3Add(results.userParserInput)
        t3Add(results.userParserInput)
    if (results.completeValue) == True:
        t3Complete(results.userParserInput)
    if (results.deleteValue) == True:
        t3Delete(results.userParserInput)
    if (results.editValue) == True:
        t3Edit(results.userParserInput)
    if (results.startValue) == True:
        t3Start(results.userParserInput)
    if (results.stopValue) == True:
        t3Stop(results.userParserInput)

if __name__ == '__main__':
    _main()

