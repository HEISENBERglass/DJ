from django.urls import path
from . import views






urlpatterns = [
	path('', views.home , name="home" ) , 
	path('blog.html' , views.blog , name="blog"),
	path('shopdet.html', views.shopdet , name='shopdet'),
	path('shopdet2.html', views.shopdet2 , name='shopdet2'),
	path('shoppingcart.html' , views.shoppingcart , name='shoppingcart'),
	path('contact.html' , views.contact , name='contact')


 
]
