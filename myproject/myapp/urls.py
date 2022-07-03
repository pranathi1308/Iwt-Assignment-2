from django.urls import path
from .views import home,register,allusers
urlpatterns = [
path('',home, name='home'),
path('register',register, name='reg'),
path('allusers',allusers, name='use'),

]