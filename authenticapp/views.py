from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'index.html')

def login(request):
    return render(request,'login.html')


def logout(request):
    pass


def sample(request):
    return render(request,'base.html')

def signup(request):
    return render(request,'signup.html')

def about(request):
    return render(request,'about.html')