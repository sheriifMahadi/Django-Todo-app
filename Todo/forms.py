from django import forms

from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['task', 'completed']
        widgets = {
            'task': forms.TextInput
            (attrs={'placeholder': "Enter new task", 'class': 'search'})}
        labels = {'task': ''}


class SearchBar(forms.Form):
    title = forms.CharField(max_length=200, label='', 
    widget=forms.TextInput(attrs={"placeholder": "Search"}))