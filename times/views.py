from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "times/index.html")

def todo(request):
    return render(request, 'times/todo.html')