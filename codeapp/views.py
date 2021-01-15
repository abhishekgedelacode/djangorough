from django.shortcuts import render
from django.http import HttpResponse
import datetime
from .models import GeeksModel
from .forms import InputForm, GeeksForm

# Create your views here.


def index(request):
    return HttpResponse("<h1>hello world codecode </h1>")


def about(request):
    return HttpResponse("<h1>this is the about page of the project</h1>")


def details(request):
    return HttpResponse("<h1> this is details page of the codeapp in codecode site</h1>")


def time_view(request):
    now = datetime.datetime.now()
    str = "Time is {}".format(now)
    return HttpResponse(str)


def list_view(request):
    context = {}
    context['dataset'] = GeeksModel.objects.all()
    return render(request, 'codeapp/index.html', context)


def form_view(request):
    context = {}
    context['form'] = InputForm()
    return render(request, 'codeapp/form.html', context)


def name_view(request):
    print(request.POST)
    return render(request, 'codeapp/name.html')
