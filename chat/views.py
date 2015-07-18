from django.shortcuts import render
from django.http import HttpResponse
from django_websocket.decorators import require_websocket

def index(request):
    return render(request, 'chat/index.html', {})
