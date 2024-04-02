from django.shortcuts import render
from django.views.decorators.http import require_GET
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from app.utils.HtmxHttpRequest import HtmxHttpRequest


@login_required
@require_GET
def index(request):
    return render(request, "home/index.html")


@require_GET
def home(request: HtmxHttpRequest) -> HttpResponse:
    return render(request, "home/home.html")
