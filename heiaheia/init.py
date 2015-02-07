#!/usr/bin/env python

'''init.py'''

import store
from models import Warrior

def _get_warriors():
	'''Get warriors from the warriors.txt file'''

	try:
		f = open('../warriors.txt')
	except IOError:
		return []

	warriors = []
	for line in f:

		line = line.strip().decode('utf-8')
		if len(line) == 0:#Skip empty lines
			continue
		if line[0] == '#':#Skip comments
			continue

		parts = line.split(':')
		name = parts[0]
		rss_id = parts[1]

		warriors.append(Warrior(name=name, rss_id=rss_id))

	return warriors

def init_warriors():
	warriors = _get_warriors()
	store.create_warriors(warriors)
