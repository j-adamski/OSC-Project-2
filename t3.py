#!/usr/bin/env python
import argparse

"""time tracker and to do list, T3. Todo list where you can add your tasks, keep track of how long you have been working on them, and save your output to a text file for additional scripting"""
"""T3 is to assist those who struggle with time management through a simple, easy to use to do list time tracker """

import datetime
import os
import json

#Commands to Implement
#t3 (b)reak 'time'
	#adds amount of time spent on a break to tracking
#t3 (o)n/start 'setup project'
	#starts/adds to time of project, making it the current tracked activity.
	#OPTIONAL: be able to say how long ago you started the activity so it can add that to the current tracked time
#t3 (f)inish/stop 'setup project'
	#saves time of current activity and stops timing it
	#TODO: finish can be swapped to stop or something else
#adding multiple tasks under one project:
	#Parse any non whitespace string followed by a colon as a project, anything after it is a task within that project
	#t3 add "project1: task four"

def t3Report():
	#t3 --report 'date' 
	#(currently defaults to entire file, timing is not implemented yet)
	#print out basic report
	#TODO add date section when timing is implemented
    inputFile = 'tasks/exampleTasks.json'
    jsonData=open(inputFile).read()
    jsonToPython = json.loads(jsonData) 

    #print statement to dump an entire json file   
    #print(json.dumps(jsonToPython, indent=4, sort_keys=True))

    #iterates through Projects and reports on their status
    for k in jsonToPython:
    	print("Projects: ",k['projectName'])
    	print("Time Spent: ", k['timeSpent'])
    	print("Completed (T/F): ",k['completed'])


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


def _main():

    """Run the CLI Interface for T3"""
    #parser
    parser = argparse.ArgumentParser()
    #save user input and print user input if they dont have a specified argument from below
    parser.add_argument('printme', help="the user input, to be printed if there are not argument flags")
    
    parser.add_argument("--add",help="Counts as a working time activity, will be saved under Projects in exampleTimedTasks",action='store_true', default=False, dest='addValue')
    parser.add_argument("--delete", help="removes activity when finished from exampleTimedTasks",action='store_true',default=False,dest='deleteValue')
    parser.add_argument("--report", help="prints out basic report of the week by default from exampleTimedTasks",action='store_true', default=False, dest='reportValue',)
    parser.add_argument("--start/on", help="starts,adds time to project, making it the current tracked activity")
    parser.add_argument("--stop/finish", help="stops timing of project, removes it as the currect tracked activity")
    parser.add_argument("--break", help="adds time spent on break to exampleTimedTasks")
    parser.add_argument("--edit",help="edits the time spent on a project", action='store_true',default=False,dest="editValue")
    results = parser.parse_args()
    print('Run Program as python3 t3.py --help for descriptions of arguments')
    print('\n')
    print('Working Flags for Now Include: --help, --report, --add')


    if (results.reportValue) == True:
        t3Report()
    if (results.addValue) == True:
        #t3Add(results.printme)
        t3Add(results.printme)
        print(results.printme + " was added successfully")
    if (results.deleteValue) == True:
        t3Delete(results.printme)
        print(results.printme + " was deleted successfully")
    if (results.editValue) == True:
        t3Edit(results.printme)
        print(results.printme + " was edited successfully")

    #t3Report()
        #t3Report('exampleTasks.txt')
if __name__ == '__main__':
	_main()

