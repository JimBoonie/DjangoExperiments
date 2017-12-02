from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Board

def home(requests):
    # return HttpResponse('Hewwo World! :DD')

    boards = Board.objects.all()
    return render(requests, 'home.html', {'boards': boards})

def board_topics(request, pk):
    board = get_object_or_404(Board, pk=pk)
    return render(request, 'topics.html', {'board': board})