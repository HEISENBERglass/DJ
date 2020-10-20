from django.shortcuts import render
marsoxod2 = "bartsucks"
def home(reguest):
		man = open("textdottext.txt" , "r")
		queen = man.read()
		dormamu = queen
		return render(reguest , 'home.html' , {'zaporoj' : dormamu})

def blog(reguest1):
	return render(reguest1, 'blog.html', {})

def shopdet(reguest2):
	return render(reguest2, 'shopdet.html' , {})

def shopdet2(reguest3):
	return render(reguest3, 'shopdet2.html' , {})

def shoppingcart(reguest4):
	return render(reguest4, 'shoppingcart.html' , {})