#!/usr/bin/env python
import argparse

"""time tracker and to do list, T3. Todo list where you can add your tasks, keep track of how long you have been working on them, and save your output to a text file for additional scripting"""

"""T3 is to assist those who struggle with time management through a simple, easy to use to do list time tracker """

import datetime
import os

import json

#Commands to Implement

#t3 (a)dd 'activity'
	#This counts as a working time activity that will be saved under projects
	#OPTIONAL: activities that end in 'break' are tagged as break time, allows you to graph time wasted
#t3 (d)elete 'activity'
	#removes activity when finished
	#TODO: should remove and mark as completed be separate things?
#t3 (r)eport 'date'
	#print out basic report of the day entered. Default is a week. #TODO: need to decide on a date format
	#Report is just a clean printout of the tasks and times, can be extended after the fact for graphs and html docs
#t3 (b)reak 'time'
	#adds amount of time spent on a break to tracking
#Starting and stopping timingDeplot
#t3 (o)n/start 'setup project'
	#starts/adds to time of project, making it the current tracked activity.
	#OPTIONAL: be able to say how long ago you started the activity so it can add that to the current tracked time
#t3 (f)inish/stop 'setup project'
	#saves time of current activity and stops timing it
	#TODO: finish can be swapped to stop or something else

#t3 help 
	#prints out help dialog

#adding multiple tasks under one project:
	#Parse any non whitespace string followed by a colon as a project, anything after it is a task within that project
	#t3 add "project1: task four"
	#t3 add "project1: task two"
	#t3 report
	#------- Projects --------
	#(0h30m) : project1: task four, task two

def t3Report():
    inputFile = 'exampleTasks.txt'
    jsonData=open(inputFile).read()
    jsonToPython = json.loads(jsonData)

    #TODO add date section
    #print('------------ ' + dateline + '------------')

    print(json.dumps(jsonToPython, indent=4, sort_keys=True))


def _main():
    """Run the CLI Interface for T3"""

    
    #parser
    parser = argparse.ArgumentParser()
    parser.add_argument("--add", help="Counts as a working time activity, will be saved under Projects in exampleTimedTasks")
    parser.add_argument("--delete", help="removes activity when finished from exampleTimedTasks")
    parser.add_argument("--report", help="prints out basic report of the week by default from exampleTimedTasks",action='store_true', default=False, dest='reportValue',)
    parser.add_argument("--start/on", help="starts,adds time to project, making it the current tracked activity")
    parser.add_argument("--stop/finish", help="stops timing of project, removes it as the currect tracked activity")
    parser.add_argument("--break", help="adds time spent on break to exampleTimedTasks")
    results = parser.parse_args()
    print('Run Program as python3 t3.py --help for descriptions of arguments')
    print('\n')
    print('Testing of Report Function Below')


    if (results.reportValue) == True:
        t3Report()
    #t3Report()
        #t3Report('exampleTasks.txt')
if __name__ == '__main__':
	_main()

