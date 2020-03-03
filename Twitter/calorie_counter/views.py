from django.shortcuts import render, redirect, HttpResponseRedirect
from .forms import FoodItemForm
from django.urls import reverse
from django.http import JsonResponse
from .models import Item
import json

# Create your views here.
def home(request):
    form = FoodItemForm()
    return render(request, 'calorie_counter/home.html', {'form': form})


def insert_item(request):
    if request.method == 'POST':
        form = FoodItemForm(request.POST)
        if form.is_valid():
            item = form.save()
            if item.brand:
                item.branded = True
                item.save()
            data = dict(form.cleaned_data.items())
            item.per_gram = data['calorie'] / data['mass']
            item.save()
        return HttpResponseRedirect(reverse('calorie_counter:home'))
    pass
# redirect(request, 'calorie_counter/home.html', {'form': form})
                
def get_name(request):
    name = request.GET.get('name')
    items = Item.objects.filter(name__startswith=name).order_by('name')[0:5].values()
    return JsonResponse({'results': list(items)})
        
        
