from django.shortcuts import render, HttpResponse
from time import gmtime, strftime
import random

def index(request):
    request.session['balance']=0
    # return HttpResponse("func works")
    mydict={}
    return render(request, 'index.html',{'mydict':mydict})

mydict=[]
def farm(request):
    location='farm'
    num= random.randint(10,20)
    request.session['balance']+=num
    time=strftime("%Y-%m-%d %H:%M %p", gmtime())
    string=f"Earned {num} golds from the {location}! {time}"
    mydict.append(string)
    return render(request,'index.html',{'mydict':mydict})

def cave(request):
    location='cave'
    num= random.randint(5,10)
    request.session['balance']+=num
    time=strftime("%Y-%m-%d %H:%M %p", gmtime())
    string=f"Earned {num} golds from the {location}! {time}"
    mydict.append(string)
    return render(request,'index.html',{'mydict':mydict})

def house(request):
    location='house'
    num= random.randint(2,5)
    request.session['balance']+=num
    time=strftime("%Y-%m-%d %H:%M %p", gmtime())
    string=f"Earned {num} golds from the {location}! {time}"
    mydict.append(string)
    return render(request,'index.html',{'mydict':mydict})

def casino(request):
    location='casino'
    num= random.randint(-50,50)
    request.session['balance']+=num
    time=strftime("%Y-%m-%d %H:%M %p", gmtime())
    if num < 0:
        num=num*-1
        lose=f"Entered a {location} and lost {num} golds...Ouch.. {time}"
        mydict.append(lose)
    else:
        win=f"Earned {num} golds from the {location}! {time}"
        mydict.append(win)
    return render(request,'index.html',{'mydict':mydict})