#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from fifo import *
from otm import *
from lru import *

# funcao principal
def main():
    # Le a quantidade de quadros disponiveis na memoria RAM
    qtd_quadros = int(sys.stdin.readline())

    # Le a lista de paginas referenciadas
    referencias = map(int, sys.stdin.readlines())

    fifo = FIFO()
    miss_fifo = fifo.execute(qtd_quadros, referencias)

    # Formata a saida
    saida = 'FIFO {0}'

    # Exibe a saida
    print(saida.format(miss_fifo))

# Verifica se e o modulo principal e executa o codigo
if __name__ == "__main__":
    main()