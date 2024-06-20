# NOTE: beautifulsoap library is required here
from bs4 import BeautifulSoup

from api import get_gadgets

soup = BeautifulSoup(get_gadgets(), 'html.parser')
print(soup)


