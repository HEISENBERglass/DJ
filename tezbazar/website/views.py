import pyttsx3
from django.shortcuts import render

def talk(word):
 engine = pyttsx3.init()
 engine.say(word)
 engine.runAndWait()

def home(reguest):
	if reguest.method == "POST":
		kabzon = reguest.POST['flint']
		talk(kabzon)
		return render(reguest , 'home.html' , {'zaporoj' : kabzon})

	else :
		return render(reguest , 'home.html' , {})

def blog(reguest1):
	return render(reguest1, 'blog.html', {})

def shopdet(reguest2):
	return render(reguest2, 'shopdet.html' , {})

def shopdet2(reguest3):
	return render(reguest3, 'shopdet2.html' , {})

def shoppingcart(reguest4):
	return render(reguest4, 'shoppingcart.html' , {})