import django_filters
from .models import*
from django_filters import DateFilter
from django import forms

COMPLETED_FILTER_CHOICES = ((True, 'Yes'), (False, 'No'))
class Search(django_filters.FilterSet):
    task = django_filters.CharFilter(lookup_expr='icontains', 
                                        widget=forms.TextInput(attrs={'placeholder': "Search for a task", 'class':'search'}))
    
    completed = django_filters.ChoiceFilter(choices = COMPLETED_FILTER_CHOICES, 
    widget=forms.Select(attrs={'class':'completed'}))
    
    class Meta:
        model = Task
        fields = '__all__'
        exclude = ['date_added']
