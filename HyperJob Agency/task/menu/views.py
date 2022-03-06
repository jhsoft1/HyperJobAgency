# from django import forms
from django.contrib.auth.models import User
from django.forms import CharField, Form
from .forms import UserCreationForm
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.views.generic import CreateView


def index_view(request):
    return render(request, "menu/menu.html")


class NewVacancyForm(Form):
    description = CharField(label='Vacancy description')


class NewResumeForm(Form):
    description = CharField(label='Resume description')


def home_view(request):
    new_resume_form = NewResumeForm()
    new_vacancy_form = NewVacancyForm()
    # success_url = 'resume/new'
    return render(request, "menu/home.html", {'new_vacancy_form': new_vacancy_form, 'new_resume_form': new_resume_form})


class MyLoginView(LoginView):
    form_class = AuthenticationForm
    redirect_authenticated_user = True
    template_name = 'menu/login.html'


class MyLogoutView(LogoutView):
    form_class = AuthenticationForm
    redirect_authenticated_user = True
    template_name = 'menu/logout.html'


class MySignupView(CreateView):
    form_class = UserCreationForm
    # form = UserCreationForm
    # model = User
    # fields = '__all__'
    success_url = 'login'
    template_name = 'menu/signup.html'
