from django.shortcuts import render

# Create your views here.
def landing(request):
    return render(request, "landing/landing.html")

def resume(request):
    return render(request, "landing/resume.html", {'title': 'experience'})

def contact(request):
    return render(request, "landing/contact.html", {'title': 'contact us'})



