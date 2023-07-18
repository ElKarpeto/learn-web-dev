from django.shortcuts import render
from django import forms
from django.urls import reverse
from django.http import HttpResponseRedirect

class NewTasksForm(forms.Form):
    task = forms.CharField(label="New Task ", min_length=2)

def index(request):
    tasks = request.session.get("tasks", [])
    """
    get() method akan mengambil dict dari session, bila 'task'
    tidak terdapat pada .session(), maka get() akan mengambil [] (list kosong)
    """
    return render(request, 'tasks/index.html', {'tasks': tasks})

def add(request):
    if request.method == "POST":
        form = NewTasksForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            tasks = request.session.get("tasks", [])
            tasks.append(task)
            request.session["tasks"] = tasks
            return HttpResponseRedirect(reverse("tasks:index"))
        else:
            return render(request, "tasks/add.html", {"form": form})
    else:
        form = NewTasksForm()
        return render(request, "tasks/add.html", {"form": form})
