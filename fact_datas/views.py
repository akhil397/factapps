from django.shortcuts import render

# Create your views here.
def index(request):#this for listing
    return render(request, 'index.html')
