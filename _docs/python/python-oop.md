---
title: Python OOP
permalink: /docs/python-oop/
---

### Instructor: Swad Tasnim, CSE-2k13


```python
class Person:
	def __init__(self,name,age,gender):
		self.name=name
		self.age=age
		self.gender=gender

	def __str__(self):
		return "name={},age={},gender={}".format(self.name,self.age,self.gender)

	def get_name(self):
		return self.name

	def get_age(self):
		return self.age

	def get_gender(self):
		return self.gender


class Student(Person):
	def __init__(s,name,age,gender,instituition,batch,roll):
		Person.__init__(s,name,age,gender)
		s.instituition=instituition
		s.batch=batch
		s.roll=roll
	def __str__(s):
		return "instituition={}, batch={}, roll={}".format(s.instituition,s.batch,s.roll)
```