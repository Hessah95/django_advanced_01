from django.shortcuts import render
from .models import Inventory
# Create your views here.

def inventory_list (request) :
	context = {
		'items' : Inventory.objects.all()
	}
	return render (request, 'list.html', context)

	