from django.urls import path
from . import views #This shows that we have imported another python(Views) file from  the same folder(LookUp)  

urlpatterns = [
    path('about.html', views.about, name="about"),
	path('', views.start, name="start"),
    path('Home.html', views.home, name="Home"),
]