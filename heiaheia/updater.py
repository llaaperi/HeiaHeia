#!/usr/bin/env python

'''updater.py'''

import parser
import store
from models import *

import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def _update_warrior(warrior):
	'''Update workout data for warrior'''
	logger.info('Update warrior '+warrior.name)
	if len(warrior.rss_id) == 0:
		return warrior
	url = 'https://www.heiaheia.com/users/%s/feed'%warrior.rss_id
	workouts = parser.parse_feed(url)
	warrior.add_workouts(workouts)
	return warrior

def _update_warriors(warriors):
	'''Update workout data for warriors'''
	for warrior in warriors:
		_update_warrior(warrior)
	return warriors

def update_all():
	'''Update all warriors existing in database'''
	warriors = store.get_warriors()
	_update_warriors(warriors)
	store.save_warriors(warriors)
