from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context_dict =  {'boldmessage':"This is a boldmessage...!!!"}
    return render(request,'rango/index.html',context=context_dict)
    #return HttpResponse("Rango says... INDEX </BR> <a href='/rango/about'>-->About</a>")


def about(request):
    context_dict = {'boldmessage': "This tutorial has been put togeter by Rambo, who soon will be rocking in Django, let's put it like that!"}
    return render(request, 'rango/about.html', context=context_dict)
    #return HttpResponse('Rango says... ABOUT </BR><a href="/rango/"">-->Index</a>')