try:
	from setuptools import setup
except:
	from distutils.core import setup

description='T3: Todo List Time Tracker'
long_description = (
        "T3 is a simple command line time tracking to do list application that is designed to assist those who struggle with time management"
        )

setup(
	name='t3',
	version="0.8",
	author="comp412GroupProject",
	author_email='thatzopoulos@luc.edu',
        description=description,
        long_description=long_description,
	url='https://github.com/j-adamski/T3-Todo-List-Time-Tracker',
        license='GPL',
	py_modules=['t3'],
	entry_points={
		'console_scripts': [
			't3 = t3:_main',
			],
	},

)

#TO RUN: sudo python3 setup.py install
#OR: just run the t3.py program because as of now there are no dependencies
