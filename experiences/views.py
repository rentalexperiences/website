from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Experience
from .forms import ExperienceForm
from django.utils import timezone
from django import forms

def index(request):
    if request.method == "POST":
        form = ExperienceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            return redirect('index')
    else:
        form = ExperienceForm()
        experiences_list = Experience.objects.all().order_by('-pk')
        recent_experiences = Experience.objects.all().order_by('-pk')[:5]
        context = {'experiences_list':experiences_list,'recent_experiences':recent_experiences,'form':form}
        return render(request, 'experiences/index.html',context)

def submit(request):
    if request.method == "POST":
        expform = ExperienceForm(request.POST, request.FILES)
        if expform.is_valid():
            expform.save()
            return redirect('index')
    else:
        expform = ExperienceForm()
    return render(request, 'experiences/submit.html',{'form':expform})
