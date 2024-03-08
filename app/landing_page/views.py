from django.shortcuts import render
from django.views.decorators.http import require_GET

def index(request):
    return render(request, "landing_page/index.html")

@require_GET
def login(request):
    return render(request, "landing_page/login.html")