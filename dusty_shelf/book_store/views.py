from django.shortcuts import render
from django.conf import settings

def test(request):
    return render(request, 'test.html')
