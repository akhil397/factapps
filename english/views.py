from django.shortcuts import render

# Create your views here.
def english(request):
    return render(request, 'english.html')