#!/usr/bin/env python
import argparse
import time
import datetime
import os
import json

"""time tracker and to do list, T3. Todo list where you can add your tasks, keep track of how long you have been working on them, and save your output to a text file for additional scripting"""
"""T3 is to assist those who struggle with time management through a simple, easy to use to do list time tracker """

def t3Report(userChoice):
	#t3 --report active/completed/all
	#(currently defaults to active, which prints out only those projects not marked completed. completed prints out only completed projects. all prints out the entire json file.
    #print out basic report

    inputFile = 'tasks/exampleTasks.json'
    jsonData=open(inputFile).read()
    jsonToPython = json.loads(jsonData) 
    
    if userChoice == 'active':
        for k in jsonToPython:
            if k['completed'] == True:
    	        print("Projects: ",k['projectName'])
    	        print("Time Spent: ", k['timeSpent'])
    elif userChoice == 'completed':
        for k in jsonToPython:
            if k['completed'] == False:
                print("Projects: ",k['projectName'])
                print("Time Spent: ", k['timeSpent'])
    elif userChoice == 'all':
        for k in jsonToPython:
    	    print("Projects: ",k['projectName'])
    	    print("Time Spent: ", k['timeSpent'])
    	    print("Completed (T/F): ",k['completed'])

    else:
        print("Invalid Option. Choose active/completed/all")
def t3Add(projectName):
	#t3 --add 'activity'
	#This counts as a working time activity that will be saved under its own project

    #new entry structure
    add_dict = {"projectName": projectName,"taskName": "","timeSpent":0,"completed":False}


    with open('tasks/exampleTasks.json') as f:
        data = json.load(f)

    data.append(add_dict)

    with open('tasks/exampleTasks.json', 'w') as f:
        json.dump(data, f)
    #TODO: add task functionality
    


def t3Delete(projectName):
	#t3 --delete 'activity'
	#removes activity when finished
	inputFile = 'tasks/exampleTasks.json'
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

	with open('tasks/exampleTasks.json', 'w') as file:
				file.write(json.dumps(list1))


def t3Edit(projectName):
	#t3 --edit 'projectName'
    #TODO the ability to edit the time of a project
    #needs to be able to check that user input the correct format
	inputFile = 'tasks/exampleTasks.json'
	jsonData=open(inputFile).read()
	data = json.loads(jsonData) 

	for k in data:
	    if projectName == k['projectName']:
	    	print("Current Time Is: " + str(k['timeSpent']))
	    	newTime = input("Enter New Time: ")
	    	k['timeSpent'] = newTime

	with open('tasks/exampleTasks.json', 'w') as f:
	    json.dump(data, f)

def t3Start(projectName):
    #t3 --start 'projectName'
    inputFile = 'tasks/timingExample.json'
    jsonData=open(inputFile).read()
    data = json.loads(jsonData)

    for k in data:
        if projectName == k['projectName']:
            print("Project Time Has Started")
            #currentTime = datetime.datetime.now().strftime('%H%M')
            k['timeStamp'] = time.time()
    with open('tasks/timingExample.json', 'w') as f:
        json.dump(data, f)

def t3Stop(projectName):
    #t3 -- stop 'projectName'
    inputFile = 'tasks/timingExample.json'
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
            #TODO change it from seconds to something cleaner looking
            print("Elapsed Time For Project: " + str(elapsedTime) + ' seconds')
            k['timeSpent'] = elapsedTime
            #reset the timestamp from json file
            k['timeStamp'] = ''
    with open('tasks/timingExample.json', 'w') as f:
        json.dump(data, f)



def _main():

    """Run the CLI Interface for T3"""
    #parser
    parser = argparse.ArgumentParser()
    #save user input and print user input if they dont have a specified argument from below
    parser.add_argument('printme', help="the user input, to be printed if there are not argument flags")
    
    parser.add_argument("--add",help="Counts as a working time activity, will be saved under Projects in exampleTimedTasks",action='store_true', default=False, dest='addValue')
    parser.add_argument("--delete", help="removes activity when finished from exampleTimedTasks",action='store_true',default=False,dest='deleteValue')
    parser.add_argument("--report", help="prints out basic report of the week by default from exampleTimedTasks",action='store_true', default=False, dest='reportValue',)
    parser.add_argument("--start", help="starts timing project worktime, will overwrite existing start time if there is one.",action='store_true',default=False,dest='startValue')
    parser.add_argument("--stop/finish", help="stops timing of project, removes that projects start time timestamp and updates the timeSpent variable",action='store_true',default=False,dest='stopValue')
    parser.add_argument("--edit",help="edits the time spent on a project", action='store_true',default=False,dest="editValue")
    results = parser.parse_args()
    print('Run Program as python3 t3.py --help for descriptions of arguments')
    print('\n')
    print('Working Flags for Now Include: --help, --report, --add')


    if (results.reportValue) == True:
        t3Report(results.printme)
    if (results.addValue) == True:
        #t3Add(results.printme)
        t3Add(results.printme)
    if (results.deleteValue) == True:
        t3Delete(results.printme)
    if (results.editValue) == True:
        t3Edit(results.printme)
    if (results.startValue) == True:
        t3Start(results.printme)
    if (results.stopValue) == True:
        t3Stop(results.printme)

    #t3Report()
        #t3Report('exampleTasks.txt')
if __name__ == '__main__':
	_main()

