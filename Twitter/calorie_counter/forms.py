from django import forms
from .models import Item

class FoodItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = {
            'name',
            'brand',
        }
        
