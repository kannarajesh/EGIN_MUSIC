from django.shortcuts import render
import os
from django.http import JsonResponse

def home_view(request):
    return render(request, 'home.html')
