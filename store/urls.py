from django.urls import path
from. import views  #due to this line if func based views u have made all will be imported at once
from .views import home , signup , login , home

urlpatterns = [ 

    #path('',views.home.index,name='homepage'),
    path('',views.home.Index.as_view(),name='homepage'),
    path('signup/',views.signup.Signup.as_view(),name='signup'),
    path('login/',views.login.Login.as_view(),name='login'),
    #path('login/',views.login,name='login'),
    #path('signup/',views.signup,name='signup'),
    #path('',views.index,name='homepage'),

]
