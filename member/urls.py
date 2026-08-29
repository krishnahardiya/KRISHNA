from django.urls import path
from . import views

urlpatterns = [
    path('',views.member,name='member'),
    path('home',views.home,name='home'),
    path('about',views.about,name='about'),
    path('product',views.product,name='product'),
    path('krishna',views.krishna,name='krishna'),
    path('myfirst',views.myfirst,name='myfirst'),
    path('contact',views.contact,name='contact'),
    path('game',views.game,name='game'),
    path('cou',views.cou,name='cou'),
    path('reg',views.reg,name='reg'),
    path('navbar',views.navbar,name='navbar'),
    path('navbarhome',views.navbarhome,name='navbarhome'),
    path('navbarabout',views.navbarabout,name='navbarabout'),
    path('navbarcontact',views.navbarcontact,name='navbarcontact'),
    path('navbarkrishna',views.navbarkrishna,name='navbarkrishna'),
    path('navbarproduct',views.navbarproduct,name='navbarproduct'),
    path('login',views.login,name='login')

         
]