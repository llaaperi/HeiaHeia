#!/usr/bin/env python

'''main.py'''

import sys
import init
import updater
import store

def main(argv=None):
	'''Main'''

	#Add all warriors to the database from the init file
	init.init_warriors()

	#Update all warriors in the database
	updater.update_all()

if __name__=="__main__":
	sys.exit(main(sys.argv))
