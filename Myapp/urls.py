
from django.urls import path
from Myapp import views

urlpatterns = [
   path('index/',views.index,name="index")
]
