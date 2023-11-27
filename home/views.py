from django.shortcuts import render
from .models import Employee
# Create your views here.
def index(request):
    data=Employee.objects.all()
    return render(request,'index.html',{'data':data})

def adddata(request):
    obj=Employee()
    obj.title=request.POST['title']
    obj.save()
    data=Employee.objects.all()
    return render(request,'index.html',{'data':data})

def updatedata(request):
    return render(request,'updatedata.html')