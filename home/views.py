from django.shortcuts import render

# Create your views here.
def home(requet):
    return render(requet,'home/home.html')