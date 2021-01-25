from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'adminp/index.html')







#webiste

def home(request):
    return render(request,'website/index.html')
