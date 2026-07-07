from django.shortcuts import render
from django.http import HttpResponse # ye import krana pdta 
# Create your views here.
def home(request): # request likhna pdta
    return HttpResponse("<h1>  welcome  </h1>")

def sum(request):
    a = 10+30
    return HttpResponse(f" the sum is : {a}")

def html(request) :# html backend ye run krana
    people = [{'name' : 'rohit' , 'age' : 21},
              {'name' : 'karan', 'age' : 22},
              {'name' : 'sagar' ,'age' : 23},
              {'name' : 'gautam', 'age' : 17}
              ]
    #ab iss dictonary ko html me table me show krne ke lie "context ka use krnege"
    return render(request,'index.html', context = {'people':people})
def contact(request) :
    return render(request,'contact.html', context = {'contact':contact})

def about(request) :
    return render(request,'about.html', context = {'about':about})
    