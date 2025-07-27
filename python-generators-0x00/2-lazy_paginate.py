#!/usr/bin/python3
paginate_users = __import__('paginate-users').paginate_users

def lazy_pagination(page_size):
    offset = 0
    while True:
        page = paginate_users(page_size, offset)
        if not page:
            break
        yield page
        offset += page_size
