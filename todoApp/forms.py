from django import forms

from .models import TodoModel


class TodoForm(forms.ModelForm):
    class Meta:
        model = TodoModel
        fields = ['title', 'description', 'priority', 'completed']
        widgets = {
            'title': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Enter title'}),
            'description': forms.Textarea(
                attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Enter description'}),
            'priority': forms.Select(
                attrs={'class': 'form-control'}),
            'completed': forms.CheckboxInput(
                attrs={'class': 'form-check-input mx-4 mt-2', 'type': 'checkbox'}),
        }
