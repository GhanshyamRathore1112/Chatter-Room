from django.shortcuts import render
from django.http import HttpResponse
from .models import Room, Topic, Message, User


def home(request):
    return HttpResponse('k')


