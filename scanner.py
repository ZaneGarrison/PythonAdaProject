#import logging
from token import Token

try:
    file = open("test1.jl", "r")
except FileNotFoundError:
    print("that file can't be accessed")
