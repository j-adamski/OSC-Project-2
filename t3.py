#!/usr/bin/env python
import argparse

"""time tracker and to do list, T3. Todo list where you can add your tasks, keep track of how long you have been working on them, and save your output to a text file for additional scripting"""

"""T3 is to assist those who struggle with time management through a simple, easy to use to do list time tracker """

import datetime
import os

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

#Starting and stopping timing
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

def t3Report(inputFile):
    file = open(inputFile, "r")
    dateline = file.readline().strip()
    #TODO, convert number string to human readable date
    print('------------ ' + dateline + '------------')
    workingTime = file.readline()
    print(workingTime)
    breakTime = file.readline()
    print(breakTime)
    
    #TODO, loop until lines that start with Projects are done, needs to check what line starts with
    for line in file:
        print(line)


def _main():
    """Run the CLI Interface for T3"""
    
    #tests on example report file, output example in directory is report.txt file
    t3Report('exampleTimedTasks.txt') 
if __name__ == '__main__':
	_main()
