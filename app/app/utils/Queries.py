from collections import namedtuple

def dictFetchAll(cursor):
    """
    Return all rows from a cursor as a dict.
    Assume the column names are unique.
    Example: [{'parent_id': None, 'id': 54360982}, {'parent_id': None, 'id': 54360880}]
    To get the value of the first row's id, use result[0]['id']
    """
    columns = [col[0] for col in cursor.description]
    return [dict(zip(columns, row)) for row in cursor.fetchall()]

def dictFetchOne(cursor):
    """
    Return one row from a cursor as a dict.
    Assume the column names are unique.
    Example: {'parent_id': None, 'id': 54360982}
    To get the value of the first row's id, use result['id']
    """
    columns = [col[0] for col in cursor.description]
    return dict(zip(columns, cursor.fetchone()))

def namedTupleFetchAll(cursor):
    """
    Return all rows from a cursor as a namedtuple.
    Assume the column names are unique.
    Example: [Result(parent_id=None, id=54360982), Result(parent_id=None, id=54360880)]
    To get the value of the first row's id, use result[0].id
    """
    desc = cursor.description
    nt_result = namedtuple("Result", [col[0] for col in desc])
    return [nt_result(*row) for row in cursor.fetchall()]

def namedTupleFetchOne(cursor):
    """
    Return one row from a cursor as a namedtuple.
    Assume the column names are unique.
    Example: Result(parent_id=None, id=54360982)
    To get the value of the first row's id, use result.id
    """
    desc = cursor.description
    nt_result = namedtuple("Result", [col[0] for col in desc])
    return nt_result(*cursor.fetchone())