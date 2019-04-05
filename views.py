from django.shortcuts import render


def index(request):
    return render(request, 'aboutme/index.html')

def django(request):
    return render(request, 'aboutme/django.html')