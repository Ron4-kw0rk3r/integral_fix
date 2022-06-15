#!/usr/bin/python3
# from codecs import namereplace_errors
import sys
# from sympy import init_session
import sympy as sym
# from __future__ import division
from sympy import *
from sympy.abc import *
import math


# init_session()


def banner():
    syym = """
        ###########################################################
    """

def  eleven():
    x, y, z = sym.symbols('x y z')
    w , t , u = sym.symbols('w, t ,u')
    k, m , n = sym.symbols('k m n' ,integer=True)
    f, g , h = sym.symbols('f, g, h')
    sym.init_printing(True)
    if  sys.argv[1] == "--mode":
        if sys.argv[2] == "--int":
            complet = pprint(str(Integral(sys.argv[3])), use_unicode=True)
            complet = pprint(Integral(sys.argv[3]), use_unicode=False)
        elif sys.argv[2] == "--der":
            complet = pprint(str(diff(sys.argv[3])), use_unicode=True)
            complet = pprint(diff(sys.argv[3]), use_unicode=False)
    else:

        name_x=input('integral : ')
        if name_x:
            complt = pprint(str(sym.diff(name_x)), use_unicode=True)
        # pprint(str(Integral(ln x, x)))
        # aprint(complt)
            pprint(Integral(sqrt(1/x), x), use_unicode=True)


if __name__ == '__main__':
    eleven()