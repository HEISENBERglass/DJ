from django.db import models

adviyats=[]


class Adverts:
	def __init__(self,name,price,description):
		self.name = name
		self.price = price
		self.description = description

class DataHolder:
	name: str
	price: str
	description : str

