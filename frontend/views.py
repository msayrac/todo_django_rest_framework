from django.shortcuts import render
from rest_framework.response import Response
from django.http import JsonResponse


# Create your views here.

def list(request):
    return render(request, 'frontend/list.html')