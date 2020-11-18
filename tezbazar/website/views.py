from django.shortcuts import render
from django.urls import path
import os
from .models import Adverts
from .models import DataHolder
from . import urls


namelist=[]
pricelist=[]
desclist=[]


def home(reguest):

	if reguest.method == "POST" :
		prname = reguest.POST['flint']
		try:
			indexOf = pricelist.index(prname)

			return shopdet(reguest ,namus=namelist[indexOf].name,prius=namelist[indexOf].price,descus=namelist[indexOf].description)

		except ValueError :
			return render(reguest , 'contact.html' , {})
	else :
		return render(reguest , 'home.html' , {})


def blog(reguest1):
	return render(reguest1, 'blog.html', {})

def shopdet(reguest2 , namus , prius , descus):
	var = DataHolder
	var.name = namus
	var.price = prius
	var.description = descus
	return render(reguest2, 'shopdet.html' , {'var' : var})

def shopdet2(reguest3):

	return render(reguest3, 'shopdet2.html' , {})

def shoppingcart(reguest4):
	return render(reguest4, 'shoppingcart.html' , {})

def contact(reguest5):
	if reguest5.method == "POST" :

		name = reguest5.POST['Name']
		price = reguest5.POST['Price']
		desc = reguest5.POST['Description']
		DataHolder.name = name
		DataHolder.price = price
		DataHolder.description = desc
		search = (DataHolder)
		namelist.append(search)
		pricelist.append(name)


	return render(reguest5, 'contact.html' , {})



