from django.shortcuts import render
from django.urls import path
import os
from .models import Adverts
from .models import DataHolder
from . import urls
import pickle

ads = []

desclist=[]


def home(reguest):

	if reguest.method == "POST" :
		zapros = reguest.POST['flint']
		f = open("dict.pickle" , "rb")
		gerald = pickle.load(f)
		dorime = gerald.name
		dorime2 = gerald.price
		dorime3 = gerald.description
		return shopdet(reguest2=reguest ,namus=dorime,prius=dorime2,descus=dorime3)
		
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
		chopin = Adverts(name,price,desc)
		sakar = open("dict.pickle" , "wb")
		pickle.dump(chopin , sakar)
		return render(reguest5 , 'contact.html' , {})

	else:
		return render(reguest5, 'contact.html' , {})



