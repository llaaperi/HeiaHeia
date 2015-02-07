#!/usr/bin/env python

'''models.py'''

import time
from sqlalchemy import *
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Warrior(Base):
	__tablename__ = 'warriors'
	id = Column(Integer, primary_key=True)
	name = Column(String(64), default='')
	rss_id = Column(String(32), default='')
	workouts = relationship('Workout', backref='warriors')

	def add_workout(self, workout):
		'''Add workout to the warrior if it does not already exist'''
		if workout not in self.workouts:
			self.workouts.append(workout)

	def add_workouts(self, workouts):
		'''Add workouts to the warrior if they do not already exist'''
		for workout in workouts:
			self.add_workout(workout)

	def __eq__(self, other):
		if self.name == other.name:
			return True
		return False

	def __repr__(self):
		str = '{Warrior name=<%s> rss_id=<%s> workouts=[%d]}'%(self.name, self.rss_id, len(self.workouts))
		return str.encode('utf-8')


class Workout(Base):
	__tablename__ = 'workouts'
	id = Column(Integer, primary_key=True)
	warrior_id = Column(Integer, ForeignKey('warriors.id'))
	sport = Column(String(64), default='')
	duration = Column(Integer, default=0)
	distance = Column(Float, default=0)
	date = Column(Integer, default=0)

	def duration_to_str(self):
		return time.strftime('%H:%M:%S', time.localtime(self.duration))

	def date_to_str(self):
		return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(self.date))

	def __eq__(self, other):
		if self.sport != other.sport:
			return False
		if self.duration != other.duration:
			return False
		if self.distance != other.distance:
			return False
		if self.date != other.date:
			return False
		return True

	def __repr__(self):
		return '{Workout sport=<%s> distance=<%.1f> duration=<%s> date=<%s>}'%(self.sport, self.distance, self.duration_to_str(), self.date_to_str())
