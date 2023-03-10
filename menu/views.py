from django.shortcuts import render
from django.http import HttpResponse
from .models import Pizza
# Create your views here.

# /menu



def index(request):
    
    '''
    #Add pizzas to view manually
    pizzas = Pizza.objects.all()
    pizzas_names = [pizza.name + ": " + str(pizza.price) + "$" for pizza in pizzas]
    pizzas_names_str = ", ".join(pizzas_names)
    return HttpResponse("Our pizzas " + pizzas_names_str)
    '''
    #add to view with HTML index file
    pizzas = Pizza.objects.all().order_by('price')
    return render(request, 'menu/index.html', { 'pizzas' : pizzas})