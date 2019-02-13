from django.shortcuts import render

def index(request):
    """ pagina principale """
    return render(request, "index.html")
