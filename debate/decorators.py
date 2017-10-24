from django import db

def get_num_queries(func):
    def wrapper(*args, **kwargs):
        db.reset_queries()
        func(*args, **kwargs)
        num_queries = sum(len(conn.queries) for conn in db.connections.all())
        return num_queries
    return wrapper

