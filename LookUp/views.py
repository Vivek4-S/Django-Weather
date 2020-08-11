from django.shortcuts import render

def home(request):
	return render(request, 'Home.html', {})

def about(request):
	return render(request, 'about.html', {})

def start(request):
	return render(request, 'start.html', {})
