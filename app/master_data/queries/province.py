from django.db import connection
from app.utils.Queries import dictFetchAll, dictFetchOne

def getProvinces(limit=None, offset=None):
    query = "SELECT * FROM master_data.province"

    if limit is not None and offset is not None:
        query += f" LIMIT {limit} OFFSET {offset}"
    with connection.cursor() as cursor:
        cursor.execute(query)
        output = dictFetchAll(cursor)

    return output

def getProvincesCount():
    query = "SELECT COUNT(*) FROM master_data.province"

    with connection.cursor() as cursor:
        cursor.execute(query)
        count = cursor.fetchone()[0]

    return count

def createProvince(name):
    with connection.cursor() as cursor:
        cursor.execute("INSERT INTO master_data.province (name) VALUES (%s) RETURNING *", [name])
        output = dictFetchOne(cursor)

    return output