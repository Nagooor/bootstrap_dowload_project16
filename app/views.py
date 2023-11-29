from django.shortcuts import render

# Create your views here.
def bootstrap_dowload(request):
    return render(request,'bootstrap_dowload.html')
    