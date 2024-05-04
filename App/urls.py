from django.urls import path
from. import views

urlpatterns = [
    path('', views.land, name='land'),
    path('SignUP_Form', views.SignUP_Form, name='SignUP_Form'),
    path('Login_Form', views.Login_Form, name='Login_FORM'),
    path('homepage', views.homepage, name='homepage'),
    path('about', views.about, name= 'about'),
    path('product', views.product, name = 'product'),
    path('blog', views.blog, name='blog'),
    path('contactus', views.contactus, name='contactus'),
    path('vegetable', views.vegetable, name='vegetable'),
    path('fruit', views.fruit, name='fruit'),
    path('search/', views.search, name='search'),
    path('logout/', views.my_logout, name='logout')
    ]