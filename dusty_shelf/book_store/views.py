from django.shortcuts import render
from django.conf import settings

def base(request):
    return render(request, 'base.html')
