from django.urls import path
from. import views


app_name='firstapp'

urlpatterns=[

   
   path('',views.index,name='index'),
   path('textpage/',views.textpage,name='textpage'),
   path('contact/',views.contact,name='contact'),
   path('login/',views.login_user,name='login'),
   path()
  

   


]