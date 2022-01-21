from django.http import HttpResponse
from django.shortcuts import render
from Event_Manager.models import Events

def index(request):
    params={'name':'krisha','place':'surat'}
    return render(request,'index.html',params)

def add_event(request):
    return render(request,'event_registration.html')

def event_submission(request):
    name=request.POST["event_name"]
    desc=request.POST["des"]
    pos_link=request.POST["poster"]
    frm_date = request.POST["fr_date"]
    to_date = request.POST["to_date"]
    deadline = request.POST["deadline"]
    email = request.POST["mail"]
    password = request.POST["pass"]

    event_info = Events(name=name,desciption=desc,poster_link=pos_link,from_dt=frm_date,to_dt=to_date,deadline=deadline,email=email,password=password)
    event_info.save()
    return render(request,'event_list.html')
