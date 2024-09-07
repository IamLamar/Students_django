from django.shortcuts import render
from .models import Student

# Create your views here.
def postlist(request):
    posts = Student.objects.all()
    return render(request,'book.html',{'posts':posts})

    
