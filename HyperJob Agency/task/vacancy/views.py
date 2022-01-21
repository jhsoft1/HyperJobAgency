from django import forms
from django.http import HttpResponse
from django.shortcuts import render, redirect
from . import models


class NewVacancyForm(forms.Form):
    description = forms.CharField(label='Vacancy description')


def index_view(request):
    return render(request, "vacancy/home.html", {'vacancies': models.Vacancy.objects.all})


def new_view(request):
    if request.method == 'GET':
        new_vacancy_form = NewVacancyForm()
        return render(request, "vacancy/new.html", {'new_vacancy_form': new_vacancy_form})
    else:
        if request.user.is_staff:
            description = request.POST.get('description')
            new_vacancy = models.Vacancy.objects.create(description=description, author=request.user)
            return redirect('/')
        else:
            return HttpResponse(status=403)
