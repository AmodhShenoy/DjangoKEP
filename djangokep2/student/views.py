from django.shortcuts import render,redirect
from .models import Student
from .forms import StudentForm

# Create your views here.
def listView(request):
    l = Student.objects.all()
    context = {'students':l}
    return render(request,'student/listView.html', context)

def detailView(request,id):
    obj = Student.objects.get(id=int(id))
    context = {'student':obj}
    return render(request,'student/detailView.html', context)

def addView(request):
    if request.method == 'GET':
        form = StudentForm()
        return render(request,'student/addView.html',{'form':form})
    else:
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
        return redirect('listView')