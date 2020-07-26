from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TodoSerializer
from .models import Todolist


class TodoView(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    queryset = Todolist.objects.all()


def index(request):
    return render(request, "build/index.html")
