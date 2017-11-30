from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Board

def home(requests):
    # return HttpResponse('Hewwo World! :DD')

    boards = Board.objects.all()
    return render(requests, 'home.html', {'boards': boards})