import functools


def owner_required(view_func):
    functools.wraps(view_func)

    def wrapper(*args, **kwargs):
        return view_func(*args, **kwargs)

    return wrapper
