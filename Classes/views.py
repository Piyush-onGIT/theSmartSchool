from django.shortcuts import render

# Create your views here.
def first(req):
    return render(req, 'index.html')

def second(req):
    return render(req, "btn.html")