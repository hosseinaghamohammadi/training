from django import forms
from .models import Item

class FoodItemForm(forms.ModelForm):
    calorie = forms.IntegerField()
    mass = forms.IntegerField()
    
    class Meta:    
        model = Item
        fields = {
            'name',
            'brand',
            'calorie',
            'mass',
        }
        
