
from django.core.paginator import Paginator

def paginator(countOfAllData,pageNumber, limit):
    paginator = Paginator([], limit)
    paginator.count = countOfAllData
    page = paginator.get_page(pageNumber)

    startNumber = (page.number - 1) * limit

    return {"page": page, "startNumber": startNumber, "limit": limit}