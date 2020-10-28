from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'scripts/index.html')


def howto(request):
    return render(request, 'scripts/howto.html', {'title': "how to use"})


def anatomy(request):
    return render(request, 'scripts/anatomy.html', {'title': 'script anatomy'})


def arm(request):
    return render(request, 'scripts/tutes/disarm.html', {'title': 'arm --> disarm'})


def addvideo(request):
    return render(request, 'scripts/tutes/addvideo.html', {'title': 'add video to fade'})


def batchadjust(request):
    return render(request, 'scripts/tutes/batchadjust.html', {'title': 'batch parameters'})


def bumplower(request):
    return render(request, 'scripts/tutes/bumplower.html', {'title': 'bump up --> lower'})


def fadein(request):
    return render(request, 'scripts/tutes/fadein.html', {'title': 'fadeout --> in'})


def projmanager(request):
    return render(request, 'scripts/tutes/projmanager.html', {'title': 'projector manager'})


def uselist(request):
    return render(request, 'scripts/tutes/uselist.html', {'title': 'use list'})

def scope(request):
    return render(request, 'scripts/tutes/scope.html', {'title': 'scope and functions'})

def resources(request):
    return render(request, 'scripts/resources.html', {'title': 'resources'})

def fadefade(request):
    return render(request, 'scripts/tutes/fadefade.html', {'title': 'fade a fade'})

