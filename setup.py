try:
	from setuptools import setup
except:
	from distutils.core import setup

setup(
	name='t3',
	version="0.10",
	author="comp412GroupProject",
	author_email='thatzopoulos@luc.edu',
	url='https://github.com/j-adamski/OSC-Project-2/',
        license='GPL',
	py_modules=['t3'],
	entry_points={
		'console_scripts': [
			't3 = t3:_main',
			],
	},

)

#TO RUN: pip install .
