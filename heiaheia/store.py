#!/usr/bin/env python

'''store.py'''

import os, sys
from models import *
from sqlalchemy.orm import sessionmaker

import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

db_path = 'sqlite:///'+os.path.dirname(__file__)+'/../warrior.db'
engine = create_engine(db_path, echo=False)
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def get_warriors():
	'''Get all warriors from database'''
	return session.query(Warrior).all()

def get_warrior(name):
	'''Get warrior by name'''
	return session.query(Warrior).filter(Warrior.name == name).first()

def create_warrior(warrior):
	'''Create warrior to the database if it does not already exist'''
	logger.info('Create warrior '+warrior.name+' with RSS id <'+warrior.rss_id+'>')
	warriors = get_warriors()
	if warrior in warriors:
		existing = get_warrior(warrior.name)
		existing.rss_id = warrior.rss_id
		session.add(existing)
	else:
		session.add(warrior)
	session.commit()


def create_warriors(warriors):
	'''Create new warriors to the database'''
	for warrior in warriors:
		create_warrior(warrior)


def save_warrior(warrior):
	'''Save warrior by updating existing or creating new'''
	session.add(warrior)
	session.commit()

def save_warriors(warriors):
	''''''
	for warrior in warriors:
		save_warrior(warrior)

def print_all():
	warriors = get_warriors()
	for warrior in warriors:
		print warrior
		for workout in warrior.workouts:
			print '  %s'%workout

def init_db():
	Base.metadata.create_all(engine)

def clear_db():
	Base.metadata.drop_all(engine)

def main(argv=None):

	option = ' '
	if len(argv) >= 2:
		option = argv[1]

	if option == 'init':
		print 'Init database'
		init_db()
		return

	if option == 'clear':
		var = raw_input("This will clear whole database. Are you sure you want to do this? (y/n))")
		if var == 'y':
			print 'Clear database'
			clear_db()
			#Initialize after clear to rebuild schema
			init_db()
		return

	if option == 'print':
		print 'Print database'
		print_all()
		return

	print 'Options: init, clear, print'

if __name__=='__main__':
	sys.exit(main(sys.argv))
