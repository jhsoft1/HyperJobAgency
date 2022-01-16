from django.shortcuts import render
from . import models


def index_view(request):
    # context = {"grouped_news": grouped_news}
    # return render(request, "news/index.html", context=context)
    return render(request, "resume/home.html", {'resumes': models.Resume.objects.all})
