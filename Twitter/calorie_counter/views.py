from django.shortcuts import render, redirect, HttpResponseRedirect
from .forms import FoodItemForm
from django.urls import reverse

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
    # form = FoodItemForm()
    return HttpResponseRedirect(reverse('calorie_counter:home'))
# redirect(request, 'calorie_counter/home.html', {'form': form})
                
        
        

