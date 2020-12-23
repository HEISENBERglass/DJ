from django.urls import path
from . import views
from . import models






urlpatterns = [
	path('', views.home , name="home" ) , 
	path('blog.html' , views.blog , name="blog"),
	path('shopdet.html', views.shopdet , name='shopdet'),
	path('shopdet2.html', views.shopdet2 , name='shopdet2'),
	path('shoppingcart.html' , views.shoppingcart , name='shoppingcart'),
	path('contact.html' , views.contact , name='contact'),
	path('login.html' , views.login , name='login'),
	path('login1.html' , views.login1 , name='login1'),




 
]
