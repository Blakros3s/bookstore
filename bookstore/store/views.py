from django.shortcuts import render

# Create your views here.
def master(request):
    return render(request,'layout/master.html')