from django.urls import path
from website import views

urlpatterns = [
    path('',views.login,name='login'),

    path('guest/',views.guest,name='guest'),
    path('register/',views.register,name='register'),
    
    path('signup/', views.signup, name='signup'),
    path('log/', views.log, name='log'), 

    path('main/',views.main,name='main'),
    path('cacal/',views.cacal,name='cacal'),
    path('recommand/',views.recommand,name='recommand'),
    path('social/',views.social,name='social'),
    path('edu/',views.edu,name='edu'),
    path('gol/',views.gol,name='gol'),
    path('copi/',views.copi,name='copi'),
    path('grap/',views.grap,name='grap'),
    path('nxtmth/',views.nxtmth,name='nxtmth'),
    path('led/',views.led,name='led'),

    path('det/',views.det,name='det'),
    path('quiz/',views.quiz,name='quiz'),
    path('research/',views.research,name='research'),

    path('profile/',views.profile,name='profile')
]
