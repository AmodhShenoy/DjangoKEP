from django.shortcuts import render

def studentView(request):
    return render(request,'student.html')