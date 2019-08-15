from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TodoSerializer
from .models import Todo


class TodoView(viewsets.ModelViewSet):
    """
    More on what viewsets are 
    https://www.django-rest-framework.org/api-guide/viewsets/

    tldr:  a type of class-based View, that does not provide any 
    method handlers such as .get() or .post(), 
    and instead provides actions such as .list() and .create()

    The viewsets base class provides the implementation for CRUD 
    operations by default, what we had to do was specify the serializer
    class and the query set.
    """
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()
