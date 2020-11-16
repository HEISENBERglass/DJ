from django.shortcuts import render
import os
import time

n = [1]

def home(reguest):
	if reguest.method == "POST" :
		prname = reguest.POST['flint']
		
		with open("textdottext.txt" , "r+") as f :
			fout = f.read()
			mackintosh = fout.replace('Delivery infomation' , prname)
			n[0] = n[0] + 1
			hello = str(str(n[0]) + ".txt")
			same = open( hello , "w+") 
			jonatan = same.write(mackintosh)
			same.close()
			thisFile = hello
			base = os.path.splitext(thisFile)[0]
			os.rename(thisFile , base + ".html")
				
		return render(reguest , 'home.html' , {'zaporoj' : prname})	



	else:
		return render(reguest , 'home.html' , {})

def blog(reguest1):
	return render(reguest1, 'blog.html', {})

def shopdet(reguest2):
	return render(reguest2, 'shopdet.html' , {})

def shopdet2(reguest3):
	return render(reguest3, 'shopdet2.html' , {})

def shoppingcart(reguest4):
	return render(reguest4, 'shoppingcart.html' , {})