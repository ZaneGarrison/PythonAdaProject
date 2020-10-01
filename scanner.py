import logging
from tokens import Tokens

#logger.basicConfig( filename='log.txt', filemode='w', format='%(name)s - %(levelname)s - %(message)s')

try:
    file = open("test1.jl", "r")
except FileNotFoundError:
    print("that file can't be accessed")


