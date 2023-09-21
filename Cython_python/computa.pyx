# # Python
# import math


# def computar(fim, inicio=1):
#     pos = inicio
#     fator = 1000 * 1000
#     while pos < fim:
#         pos += 1
#         math.sqrt((pos - fator) * (pos - fator))

################################################################################

# # Cython
# import cython
# from libc.math cimport sqrt


# def computar(fim: cython.int, inicio: cython.int = 1):
#     pos: cython.int = inicio
#     fator: cython.int = 1000 * 1000
#     while pos < fim:
#         pos += 1
#         sqrt((pos - fator) * (pos - fator))

################################################################################

# C
import cython
from libc.math cimport sqrt


def computar(fim: cython.int, inicio: cython.int = 1):
    pos: cython.int = inicio
    fator: cython.int = 1000 * 1000

    with nogil: # Gerenciado de contexto (sem o gil, usa o c apenas?)
        while pos < fim:
            pos += 1
            sqrt((pos - fator) * (pos - fator))
