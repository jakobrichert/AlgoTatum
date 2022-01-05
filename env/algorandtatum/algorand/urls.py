from django.urls import path
from . import views

app_name = 'algorand'

urlpatterns = [
    path('', views.index, name="index"), path('404.html', views.four, name = "four"), 
     
    
    path('explores.html', views.explore, name = "explore"),  
    path("item-details.html", views.itemdetails, name = "item-details"), 
    path("live.html", views.live, name = "live"),
    path("signin.html", views.signin, name = "signin"),
    path("signup.html", views.signup, name = "signup"), 
    path("wallet.html", views.wallet, name = "wallet"),
    path("index.html", views.index, name="index"),
    

]