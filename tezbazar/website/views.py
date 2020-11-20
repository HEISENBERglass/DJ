from django.shortcuts import render
from django.urls import path
import os
from .models import Adverts
from .models import DataHolder
from . import urls

ads = []
nemes = []
desclist=[]


def home(reguest):

	if reguest.method == "POST" :
		prname = reguest.POST['flint']
		try:

			if prname in nemes:
				indexOf = nemes.index(prname)
				return shopdet(reguest ,namus=ads[indexOf].name,prius=ads[indexOf].price,descus=ads[indexOf].description)
			else:
				return shopdet(reguest,namus="lox",prius="ti",descus="ne smoq")
		except ValueError :
			return render(reguest , 'contact.html' , {})
	else :
		return render(reguest , 'home.html' , {})


def blog(reguest1):
	return render(reguest1, 'blog.html', {})

def shopdet(reguest2 , namus , prius , descus):

	DataHolder.name=namus
	DataHolder.price=prius
	DataHolder.description=descus
	var = DataHolder


	return render(reguest2, 'shopdet.html' , {'var' : var})

def shopdet2(reguest3):

	return render(reguest3, 'shopdet2.html' , {})

def shoppingcart(reguest4):
	return render(reguest4, 'shoppingcart.html' , {})

def contact(reguest5):
	if reguest5.method == "POST" :

		name = str(reguest5.POST['Name'])
		price = str(reguest5.POST['Price'])
		desc = str(reguest5.POST['Description'])
		search = Adverts(name,price,desc)
		nemes.append(name)
		ads.append(search)


	return render(reguest5, 'contact.html' , {})



