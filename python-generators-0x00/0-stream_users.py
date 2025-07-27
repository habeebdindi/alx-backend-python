#!/usr/bin/env python3

seed = __import__(seed)
connection = seed.connect_to_prodev()

def stream_users():
    """A generator that streams rows from an SQL database one by one."""
    
