from django.shortcuts import render

# Create your views here.
def igate(request):
    return render(request,'igate.html')

def airport(request):
    return render(request,'airport.html')