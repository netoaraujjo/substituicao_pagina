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

    # Instancia um objeto da class FIFO
    fifo = FIFO()
    # Executa o algoritmo de escalonamento FIFO
    miss_fifo = fifo.execute(qtd_quadros, referencias)

    # Instancia um objeto da class OTM
    otm = OTM()
    # Executa o algoritmo de escalonamento OTM
    miss_otm = otm.execute(qtd_quadros, referencias)

    # Instancia um objeto da class LRU
    lru = LRU()
    # Executa o algoritmo de escalonamento LRU
    miss_lru = lru.execute(qtd_quadros, referencias)

    # Formata a saida
    saida = 'FIFO {0}\nOTM {1}\nLRU {2}'

    # Exibe a saida
    print(saida.format(miss_fifo, miss_otm, miss_lru))


# Verifica se e o modulo principal e executa o codigo
if __name__ == "__main__":
    main()
