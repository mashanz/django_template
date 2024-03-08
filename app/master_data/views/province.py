from django.shortcuts import render
from django.views.decorators.http import require_GET, require_POST
from app.utils.HtmxHttpRequest import HtmxHttpRequest
from django.http import HttpResponse
from master_data.queries.province import getProvinces, createProvince, getProvincesCount
from django.core.paginator import Paginator

# Create your views here.
@require_GET
def index(request):
    return render(request, "master_data/province/index.html")

@require_GET
def table(request: HtmxHttpRequest) -> HttpResponse:
    pageNumber = request.GET.get("page", "1")
    limit = 3
    provinces = getProvinces(limit=limit, offset=(int(pageNumber) - 1) * limit)

    paginator = Paginator(provinces, limit)
    paginator.count = getProvincesCount()
    page = paginator.get_page(pageNumber)

    startNumber = (page.number - 1) * limit

    return render(request, 
                  "master_data/province/table.html",
                  {"provinces": provinces, "page": page, "startNumber": startNumber, "limit": limit})

@require_GET
def add(request: HtmxHttpRequest) -> HttpResponse:
    return render(request, "master_data/province/add.html")

@require_POST
def create(request: HtmxHttpRequest):
    createProvince(request.POST.get("name"))

    return render(request, "master_data/province/loader.html")