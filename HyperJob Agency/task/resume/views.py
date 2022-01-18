from django import forms
from django.shortcuts import render, redirect
from . import models


class NewResumeForm(forms.Form):
    description = forms.CharField(label='Resume description')


def new_view(request):
    if request.method == 'GET':
        new_resume_form = NewResumeForm()
        return render(request, "resume/new.html", {'new_resume_form': new_resume_form})
    else:
        description = request.POST.get('description')
        new_resume = models.Resume.objects.create(description=description, author=request.user)
        return redirect('/')


def index_view(request):
    return render(request, "resume/home.html", {'resumes': models.Resume.objects.all})
