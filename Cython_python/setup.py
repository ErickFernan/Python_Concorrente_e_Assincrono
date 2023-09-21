# Arquivo python com as informações dos modulo Cython que eu desejo compilar
from distutils.core import setup
from Cython.Build import cythonize

setup(
    ext_modules=cythonize(['cumprimenta.pyx', 'computa.pyx'])
)

# Para executar o arquivo.pyx é preciso compilar usando "python3 setup.py build_ext --inplace"