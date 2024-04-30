from  django.shortcuts import render,HttpResponse


def home(requests):
    return HttpResponse("hello world")
