from django import forms
from django.forms import ModelForm
from .models import *

class TaskForm(forms.ModelForm):
	title= forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Task title...'}), label=False)
	due= forms.DateTimeField(
		widget= forms.DateTimeInput(attrs={
			'placeholder':'Due date (YYYY-MM-DD HH:MM)...', 
			'type': 'datetime-local'
		}), 
		label=False, 
		required=False
	)

	class Meta:
		model = task
		fields = ['title', 'due']


class UpdateForm(forms.ModelForm):
	title= forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Task title...'}))

	class Meta:
		model = task
		fields = ['title', 'due', 'complete']