from django.shortcuts import render

def index(request):
    return render(request, 'first/index.html')

def about(request):
    return render(request, 'first/about.html')
