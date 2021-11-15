from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request):
 #return HttpResponse("DEUSTO MOTO TEAM. Web en desarrollo.")
 return render(request, "index.html")