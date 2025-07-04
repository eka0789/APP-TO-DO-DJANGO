from django.shortcuts import render, redirect, get_object_or_404

from .models import *
from .forms import *

def listTask(request):
	queryset = task.objects.order_by('complete','due')
	form = TaskForm()
	if request.method =='POST':
		form = TaskForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('/')
	context = {
		'tasks':queryset,
		'form':form,
		}
	return render(request, 'list_task.html', context)


def updateTask(request, pk):
	queryset = get_object_or_404(task, id=pk)
	form = UpdateForm(instance=queryset)
	if request.method == 'POST':
		form = UpdateForm(request.POST, instance=queryset)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {
		'form':form
		}

	return render(request, 'update_task.html', context)


def deleteTask(request, pk):
	queryset = get_object_or_404(task, id=pk)
	if request.method == 'POST':
		queryset.delete()
		return redirect('/')

	context = {
		'item':queryset
		}
	return render(request, 'delete_task.html', context)
