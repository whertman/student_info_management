from django.shortcuts import (get_object_or_404, render, HttpResponseRedirect)
from django.http import HttpResponse
from .models import Student
from .forms import Student_Name
# Create your views here.

# Student views
def list_view(request):
    context = {}
    context["dataset"] = Student.objects.all()
    return render(request, "list_view.html", context)

def create_view(request):
    context = {}
    form = Student_Name(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("../")
    context['form'] = form
    return render(request, "create_view.html", context)

def detail_view(request, id):
    context={}
    context["data"] = Student.objects.get(id = id)
    return render(request, "detail_view.html", context)

def update_view(request, id):
    context={}
    obj = get_object_or_404(Student, id = id)
    form = Student_Name(request.POST or None, instance = obj)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("../"+id)
    context["form"] = form
    return render(request, "update_view.html", context)

def delete_view(request, id):
    context={}
    obj = get_object_or_404(Student, id = id)
    if request.method =="POST":
        obj.delete()
        return HttpResponseRedirect("../")
    return render(request, "delete_view.html", context)

