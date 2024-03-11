from django.shortcuts import render
from django.views.decorators.http import require_GET, require_POST
from app.utils.HtmxHttpRequest import HtmxHttpRequest
from django.http import HttpResponse
from master_data.queries.province import getProvinces, createProvince, getProvincesCount
from app.utils.Pagination import paginator

# Create your views here.
@require_GET
def index(request):
    return render(request, "master_data/province/index.html")

@require_GET
def table(request: HtmxHttpRequest) -> HttpResponse:
    pageNumber = request.GET.get("page", "1")
    limit = 3
    provinces = getProvinces(limit=limit, offset=(int(pageNumber) - 1) * limit)
    countOfAllData = getProvincesCount()

    pagination = paginator(countOfAllData, pageNumber, limit)

    return render(request, "master_data/province/table.html", {"provinces": provinces, "pagination": pagination})

@require_GET
def add(request: HtmxHttpRequest) -> HttpResponse:
    return render(request, "master_data/province/add.html")

@require_POST
def create(request: HtmxHttpRequest):
    createProvince(request.POST.get("name"))

    return render(request, "master_data/province/loader.html")