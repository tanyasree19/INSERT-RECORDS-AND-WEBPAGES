from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from app.forms import *
def insert_topic(request):
    tf=TopicForm()
    d={'tf':tf}
    if request.method=='POST':
        FD=TopicForm(request.POST)
        if FD.is_valid():
            FD.save()
            return HttpResponse('Data inserted')

    return render(request,'insert_topic.html',d)

def insert_webpage(request):
    wf=WebpageForm()
    d={'wf':wf}
    if request.method=='POST':
        FD=WebpageForm(request.POST)
        if FD.is_valid():
            FD.save()
            return HttpResponse('webpage is inserted')
    return render(request,'insert_webpage.html',d)

def insert_records(request):
    rf=RecordsForm()
    d={'rf':rf}
    if request.method=='POST':
        FD=RecordsForm(request.POST)
        if FD.is_valid():
            FD.save()
            return HttpResponse('record inserted successful')
    return render(request,'insert_records.html',d)

