
from django.core.paginator import Paginator

# This function is used to paginate the data
# countOfAllData: The total number of data
# pageNumber: The current page number
# limit: The number of data to be displayed per page
def paginator(countOfAllData,pageNumber, limit):
    paginator = Paginator([], limit)
    paginator.count = countOfAllData
    page = paginator.get_page(pageNumber)

    startNumber = (page.number - 1) * limit

    return {"page": page, "startNumber": startNumber, "limit": limit}