from django.urls import path
from .import views

urlpatterns = [
   path('',views.admin_signin,name='admin_signin'),
   path('admin_signout/',views.admin_signout,name='admin_signout'),
   path('admin_home/',views.admin_home,name='adminhome'),
   
    
]
