from django.shortcuts import render
import os
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def home_view(request):
    return render(request, 'home.html')
