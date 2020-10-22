from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'scripts/index.html')

def how_to(request):
    return render(request, 'scripts/how_to.html', {'title': "roboscripts - how to use"})

def arm(request):
    return render(request, 'scripts/arm.html', {'title': 'convert disarm to arm'})
