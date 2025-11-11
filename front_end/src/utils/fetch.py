import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))
import requests as req
from src import widgets

def get_items() -> bytes:
    return req.get(
        url="http://localhost:8000/items/50"
    ).content

if __name__ == '__main__':
    widgets.table.table()
    print("Test string")
