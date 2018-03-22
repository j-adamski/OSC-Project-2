# T3: Todo List Time Tracker

<b>Mission Statement: </b> To assist those who struggle with time management through a simple, easy to use to do list time tracker

<b>Placeholder for pic: </b>
TODO

<b>License: </b>
GPL 3.0 

<b>Installation/Compiling:</b>
Full Instructions can be found in [GettingStarted.md](https://github.com/j-adamski/T3-Todo-List-Time-Tracker/blob/master/GettingStarted.md)


# Features List/Commands Left To Implement:

- `python t3.py --add 'project name'`
	#This counts as a working time activity that will be saved under projects
	#OPTIONAL: activities that end in 'break' are tagged as break time, allows you to graph time wasted

- `python t3.py --delete 'project name'`
	#removes activity when finished
	
- `python t3.py --edit 'project name'`	
	#edits the time spent doing the activity	

 - `python t3.py --break 'time'`
	#adds amount of time spent on a break to tracked project

- `python t3.py --report 'date'`
	#print out basic report of the day entered. Default is a week. #TODO: need to decide on a date format
	#Report is just a basic clean printout of the tasks and times to terminal


<b>Starting and stopping timing</b>
 - `python t3.py --start 'project name'`
	#starts/adds to time of project, making it the current tracked activity.

 - `python t3.py --finish 'project name'`
	#saves time of current activity and stops timing it

 - `python t3.py --help `
	#prints out help dialog

Robust Report Command that generates nice CSS, HTML, etc. graphs and charts of time spent on various projects, time wasted, etc. if time permits. 

# [FAQ](https://github.com/j-adamski/OSC-Project-2/wiki): (Rest of FAQ Can Be Found In The Wiki)

Q: Is T3 Open Source?

    Yes, T3 is licensed under the GPL and created by students at Loyola University Chicato attending the Open Source Computing Class

Q: When was T3 started?

    Spring 2018

Q: Where can I talk about development of T3?

    The IRC Chanel on Freenode can be joined with the following command:
    /join ##T3Comp412


