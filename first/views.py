from django.shortcuts import render
from first.namer import bob
import os

def home(request):
	my_name = "Hello. My name is Michael Abreu."
	alt_string = str(os.environ.get('SECRET_KEY'))
	return render(request, "home.html", {"bob": alt_string})

def about(request):
	return render(request, "about.html", {})

def main_route(request):
	return render(request, "index.html")

def contact(request):
	return render(request, "contact.html", {"my_stuff": bob})