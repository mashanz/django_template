from django.urls import include, path

from .views import province

province_urlpatterns = (
    [
        path("index", province.index, name="index"),
        path("table", province.table, name="table"),
        path("add", province.add, name="add"),
        path("create", province.create, name="create"),
    ],
    "province",
)

urlpatterns = [
    path("province/", include(province_urlpatterns, namespace="province")),
]

app_name = "master_data"
