from django.shortcuts import render
from . import models


def index_view(request):
    return render(request, "vacancy/home.html", {'vacancies': models.Vacancy.objects.all})
