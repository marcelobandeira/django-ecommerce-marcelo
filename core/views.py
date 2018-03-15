from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
	texts = ['Lorem ipsum dolor sit amet', 'consectetur adipisicing elit']
	context = {
		'title': 'django e-commerce',
		'texts': texts
	}

	return render(request, 'index.html', context)

def contact(request):
	return render(request, 'contact.html')

def product_list(request):
	return render(request, 'product_list.html')

def product(request):
	return render(request, 'product.html')